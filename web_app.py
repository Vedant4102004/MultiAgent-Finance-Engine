import streamlit as st
import os
from dotenv import load_dotenv
from models.load_models import load_llm
from agents.bull_agent import create_bull_agent
from agents.bear_agent import create_bear_agent
from agents.risk_agent import create_risk_agent
from agents.judge_agent import create_judge_agent
from tools.data_fetcher import format_market_data, format_news
from tools.portfolio_analyzer import analyze_portfolio, calculate_portfolio_weights, get_portfolio_summary
from langchain_core.runnables import RunnableParallel

load_dotenv()

st.set_page_config(
    page_title="💰 Finance Debate Engine",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 20px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize LLM and agents
@st.cache_resource
def load_agents():
    llm = load_llm()
    bull = create_bull_agent(llm)
    bear = create_bear_agent(llm)
    risk = create_risk_agent(llm)
    judge = create_judge_agent(llm)
    
    parallel = RunnableParallel(
        bull_case=bull,
        bear_case=bear,
        risk_case=risk
    )
    
    return parallel, judge, llm

def run_analysis(query, company_name, parallel, judge):
    """Run investment analysis for a company"""
    
    # Fetch real market data and news
    market_data = format_market_data(company_name)
    news = format_news(company_name)
    
    results = parallel.invoke({
        "query": query,
        "market_data": market_data,
        "news": news,
        "rag_context": ""
    })

    final = judge.invoke({
        "bull_case": results["bull_case"],
        "bear_case": results["bear_case"],
        "risk_case": results["risk_case"]
    })

    return results, final, market_data, news

# Title
st.title("💰 Multi-Agent Finance Debate Engine")
st.markdown("AI-powered investment analysis with portfolio tracking")

# Load agents
parallel, judge, llm = load_agents()

# Sidebar
with st.sidebar:
    st.header("📌 Navigation")
    page = st.radio(
        "Select Analysis Type:",
        ["🏢 Single Stock Analysis", "🎯 Portfolio Analysis", "📊 Market Overview"]
    )

# Single Stock Analysis
if page == "🏢 Single Stock Analysis":
    st.header("🏢 Single Stock Analysis")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        company = st.text_input(
            "Enter company name (e.g., Apple, Microsoft, Reliance):",
            value="Apple",
            placeholder="Type company name or ticker..."
        )
    
    with col2:
        analyze_btn = st.button("🚀 Analyze", use_container_width=True)
    
    if analyze_btn and company:
        with st.spinner(f"🔍 Analyzing {company}..."):
            query = f"Should I invest in {company}?"
            
            try:
                results, final, market_data, news = run_analysis(query, company, parallel, judge)
                
                # Display Market Data
                st.subheader("📊 Market Data")
                st.markdown(market_data)
                
                # Display News
                st.subheader("📰 Latest News")
                st.markdown(news)
                
                # Display Agent Cases
                st.subheader("🤖 Agent Analysis")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.success("🐂 Bull Case")
                    st.info(results["bull_case"])
                
                with col2:
                    st.error("🐻 Bear Case")
                    st.warning(results["bear_case"])
                
                with col3:
                    st.info("⚠️ Risk Analysis")
                    st.write(results["risk_case"])
                
                # Display Final Recommendation
                st.subheader("⚖️ Judge's Final Verdict")
                st.success(final)
                
            except Exception as e:
                st.error(f"❌ Error analyzing {company}: {str(e)}")

# Portfolio Analysis
elif page == "🎯 Portfolio Analysis":
    st.header("🎯 Portfolio Analysis")
    
    st.markdown("**Add multiple companies to analyze your portfolio**")
    
    # Input for multiple companies
    portfolio_input = st.text_area(
        "Enter company names (one per line):",
        value="Apple\nMicrosoft\nGoogle",
        height=150,
        placeholder="Apple\nMicrosoft\nGoogle\n..."
    )
    
    if st.button("📈 Analyze Portfolio", use_container_width=True):
        companies = [c.strip() for c in portfolio_input.split('\n') if c.strip()]
        
        if companies:
            with st.spinner("📊 Analyzing portfolio..."):
                # Portfolio Summary
                st.subheader("📊 Portfolio Summary")
                
                summary = get_portfolio_summary(companies)
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Total Companies", len(companies))
                with col2:
                    st.metric("Avg Portfolio Return", summary["avg_return"])
                with col3:
                    st.metric("Avg P/E Ratio", summary["avg_pe"])
                with col4:
                    st.metric("Sector Diversity", summary["sector_diversity"])
                
                # Portfolio Data Table
                st.subheader("💼 Holdings")
                portfolio_result = analyze_portfolio(companies)
                
                if portfolio_result["portfolio_data"] is not None:
                    st.dataframe(
                        portfolio_result["portfolio_data"],
                        use_container_width=True,
                        hide_index=True
                    )
                
                # Portfolio Weights
                st.subheader("⚖️ Portfolio Weights")
                weights_df = calculate_portfolio_weights(companies)
                
                if weights_df is not None:
                    st.dataframe(
                        weights_df,
                        use_container_width=True,
                        hide_index=True
                    )
                    
                    # Pie chart
                    weights_df["Weight"] = weights_df["Weight (%)"].str.replace("%", "").astype(float)
                    chart_data = weights_df[["Company", "Weight"]].set_index("Company")
                    st.bar_chart(chart_data)
                
                # Individual Analysis
                st.subheader("📋 Individual Stock Analysis")
                
                for company in companies:
                    with st.expander(f"📌 {company.upper()}"):
                        try:
                            query = f"Should I invest in {company}?"
                            results, final, market_data, news = run_analysis(
                                query, company, parallel, judge
                            )
                            
                            st.markdown("**Recommendation:**")
                            st.success(final)
                        except Exception as e:
                            st.error(f"Error analyzing {company}: {str(e)}")
        else:
            st.warning("Please enter at least one company name")

# Market Overview
elif page == "📊 Market Overview":
    st.header("📊 Market Overview")
    
    st.info("💡 Compare multiple companies and get detailed analysis")
    
    # Preset portfolios
    col1, col2, col3 = st.columns(3)
    
    preset_portfolios = {
        "Tech Giants": ["Apple", "Microsoft", "Google"],
        "Indian Leaders": ["Reliance", "Tata", "Infosys"],
        "Mixed Portfolio": ["Apple", "Reliance", "Microsoft"]
    }
    
    selected_portfolio = st.radio(
        "Select a preset portfolio or create your own:",
        list(preset_portfolios.keys()) + ["Custom"]
    )
    
    if selected_portfolio == "Custom":
        companies = st.multiselect(
            "Select companies:",
            ["Apple", "Microsoft", "Google", "Amazon", "Meta",
             "Reliance", "Tata", "Infosys", "HCL", "Wipro"]
        )
    else:
        companies = preset_portfolios[selected_portfolio]
        st.write(f"📌 Analyzing: {', '.join(companies)}")
    
    if st.button("🔍 Compare Portfolio"):
        if companies:
            with st.spinner("Analyzing market data..."):
                summary = get_portfolio_summary(companies)
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("📊 Companies", len(companies))
                with col2:
                    st.metric("📈 Avg Return", summary["avg_return"])
                with col3:
                    st.metric("💹 Avg P/E", summary["avg_pe"])
                with col4:
                    st.metric("🌍 Sector Diversity", summary["sector_diversity"])
                
                portfolio_result = analyze_portfolio(companies)
                if portfolio_result["portfolio_data"] is not None:
                    st.dataframe(
                        portfolio_result["portfolio_data"],
                        use_container_width=True,
                        hide_index=True
                    )
        else:
            st.warning("Please select at least one company")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
    💡 Powered by: LangChain • yfinance • Finnhub • Streamlit<br>
    ⚠️ Disclaimer: This is for educational purposes only. Not financial advice.
</div>
""", unsafe_allow_html=True)
