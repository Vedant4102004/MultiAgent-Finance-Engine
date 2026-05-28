import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from models.load_models import load_llm
from agents.bull_agent import create_bull_agent
from agents.bear_agent import create_bear_agent
from agents.risk_agent import create_risk_agent
from agents.judge_agent import create_judge_agent
from tools.data_fetcher import format_market_data, format_news

from langchain_core.runnables import RunnableParallel

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

def run(query, company_name):
    
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

    return final


if __name__ == "__main__":
    company = input("Enter company name (e.g., Apple, Reliance, Microsoft): ")
    query = f"Should I invest in {company}?"
    print(f"\n📊 Analyzing: {query}\n")
    print("Fetching market data and news...")
    result = run(query, company)
    print(f"\n{result}")

