import yfinance as yf
import finnhub
import os
from typing import Dict

def get_stock_ticker(company_name: str) -> str:
    """Convert company name to ticker symbol"""
    # Common mappings
    ticker_map = {
        "reliance": "RELIANCE.NS",
        "tata": "TATA.NS",
        "one8": "ONE8.NS",  # Adjust as needed
        "apple": "AAPL",
        "microsoft": "MSFT",
        "google": "GOOGL",
        "amazon": "AMZN",
    }
    return ticker_map.get(company_name.lower(), company_name.upper())


def get_stock_data(company_name: str) -> Dict:
    """Fetch stock data from yfinance"""
    try:
        ticker = get_stock_ticker(company_name)
        stock = yf.Ticker(ticker)
        
        # Get historical data
        hist = stock.history(period="1y")
        
        # Get company info
        info = stock.info
        
        return {
            "ticker": ticker,
            "current_price": info.get("currentPrice", "N/A"),
            "market_cap": info.get("marketCap", "N/A"),
            "pe_ratio": info.get("trailingPE", "N/A"),
            "dividend_yield": info.get("dividendYield", "N/A"),
            "52_week_high": info.get("fiftyTwoWeekHigh", "N/A"),
            "52_week_low": info.get("fiftyTwoWeekLow", "N/A"),
            "avg_volume": info.get("averageVolume", "N/A"),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A"),
            "1_year_return": f"{((hist['Close'].iloc[-1] / hist['Close'].iloc[0] - 1) * 100):.2f}%" if len(hist) > 0 else "N/A",
        }
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return {}


def get_company_news(company_name: str, limit: int = 5) -> list:
    """Fetch latest news from Finnhub (requires API key)"""
    from datetime import datetime, timedelta
    
    api_key = os.getenv("FINNHUB_API_KEY")
    
    if not api_key:
        print("⚠️  Finnhub API key not set. Using yfinance news only.")
        return []
    
    try:
        finnhub_client = finnhub.Client(api_key=api_key)
        ticker = get_stock_ticker(company_name)
        
        # Get news from last 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        
        news = finnhub_client.company_news(
            ticker,
            _from=start_date.strftime("%Y-%m-%d"),
            to=end_date.strftime("%Y-%m-%d")
        )
        
        return [
            {
                "headline": item.get("headline"),
                "summary": item.get("summary"),
                "source": item.get("source"),
                "url": item.get("url"),
            }
            for item in news[:limit]
        ]
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []


def get_company_info(company_name: str) -> Dict:
    """Get company fundamentals"""
    try:
        ticker = get_stock_ticker(company_name)
        stock = yf.Ticker(ticker)
        info = stock.info
        
        return {
            "name": info.get("longName", company_name),
            "description": info.get("longBusinessSummary", "N/A"),
            "website": info.get("website", "N/A"),
            "employees": info.get("fullTimeEmployees", "N/A"),
            "debt_to_equity": info.get("debtToEquity", "N/A"),
            "return_on_equity": info.get("returnOnEquity", "N/A"),
            "profit_margin": info.get("profitMargins", "N/A"),
        }
    except Exception as e:
        print(f"Error fetching company info: {e}")
        return {}


def format_market_data(company_name: str) -> str:
    """Format market data for LLM context"""
    stock_data = get_stock_data(company_name)
    company_info = get_company_info(company_name)
    
    if not stock_data:
        return "Market data unavailable"
    
    formatted = f"""
📊 MARKET DATA FOR {stock_data.get('ticker', 'N/A')}:
- Current Price: ${stock_data.get('current_price', 'N/A')}
- Market Cap: ${stock_data.get('market_cap', 'N/A')}
- P/E Ratio: {stock_data.get('pe_ratio', 'N/A')}
- Dividend Yield: {stock_data.get('dividend_yield', 'N/A')}
- 52 Week High: ${stock_data.get('52_week_high', 'N/A')}
- 52 Week Low: ${stock_data.get('52_week_low', 'N/A')}
- 1 Year Return: {stock_data.get('1_year_return', 'N/A')}
- Sector: {stock_data.get('sector', 'N/A')}
- Industry: {stock_data.get('industry', 'N/A')}
- Debt to Equity: {company_info.get('debt_to_equity', 'N/A')}
- Return on Equity: {company_info.get('return_on_equity', 'N/A')}
"""
    return formatted


def format_news(company_name: str) -> str:
    """Format news for LLM context"""
    news = get_company_news(company_name)
    
    if not news:
        return "No recent news available"
    
    formatted = "📰 RECENT NEWS:\n"
    for i, article in enumerate(news, 1):
        formatted += f"\n{i}. {article.get('headline', 'N/A')}\n   Source: {article.get('source', 'N/A')}\n"
    
    return formatted
