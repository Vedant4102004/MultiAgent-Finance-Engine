from typing import List, Dict
from tools.data_fetcher import get_stock_data, format_market_data
import pandas as pd


def analyze_portfolio(companies: List[str]) -> Dict:
    """Analyze a portfolio of multiple companies"""
    
    portfolio_data = []
    total_market_cap = 0
    
    for company in companies:
        try:
            stock_data = get_stock_data(company)
            if stock_data:
                portfolio_data.append({
                    "Company": company.upper(),
                    "Ticker": stock_data.get("ticker", "N/A"),
                    "Current Price": stock_data.get("current_price", "N/A"),
                    "Market Cap": stock_data.get("market_cap", "N/A"),
                    "P/E Ratio": stock_data.get("pe_ratio", "N/A"),
                    "Sector": stock_data.get("sector", "N/A"),
                    "1Y Return": stock_data.get("1_year_return", "N/A"),
                })
                if isinstance(stock_data.get("market_cap"), (int, float)):
                    total_market_cap += stock_data["market_cap"]
        except Exception as e:
            print(f"Error processing {company}: {e}")
            continue
    
    return {
        "portfolio_data": pd.DataFrame(portfolio_data) if portfolio_data else None,
        "total_companies": len(portfolio_data),
        "total_market_cap": total_market_cap,
    }


def calculate_portfolio_weights(companies: List[str]) -> pd.DataFrame:
    """Calculate portfolio weights based on market cap"""
    
    weights_data = []
    total_market_cap = 0
    market_caps = {}
    
    # Get all market caps
    for company in companies:
        try:
            stock_data = get_stock_data(company)
            if stock_data and isinstance(stock_data.get("market_cap"), (int, float)):
                market_caps[company] = stock_data["market_cap"]
                total_market_cap += stock_data["market_cap"]
        except:
            pass
    
    # Calculate weights
    for company, market_cap in market_caps.items():
        if total_market_cap > 0:
            weight = (market_cap / total_market_cap) * 100
            weights_data.append({
                "Company": company.upper(),
                "Market Cap": f"${market_cap:,.0f}",
                "Weight (%)": f"{weight:.2f}%"
            })
    
    return pd.DataFrame(weights_data) if weights_data else None


def get_portfolio_summary(companies: List[str]) -> Dict:
    """Get summary statistics for portfolio"""
    
    total_return = 0
    avg_pe = 0
    sectors = {}
    count = 0
    
    for company in companies:
        try:
            stock_data = get_stock_data(company)
            if stock_data:
                # Parse 1Y return
                return_str = str(stock_data.get("1_year_return", "0%")).replace("%", "")
                try:
                    total_return += float(return_str)
                except:
                    pass
                
                # Parse P/E
                pe_str = stock_data.get("pe_ratio", 0)
                try:
                    avg_pe += float(pe_str)
                except:
                    pass
                
                # Track sectors
                sector = stock_data.get("sector", "Unknown")
                sectors[sector] = sectors.get(sector, 0) + 1
                
                count += 1
        except:
            pass
    
    return {
        "avg_return": f"{(total_return / count):.2f}%" if count > 0 else "N/A",
        "avg_pe": f"{(avg_pe / count):.2f}" if count > 0 else "N/A",
        "top_sector": max(sectors, key=sectors.get) if sectors else "N/A",
        "sector_diversity": len(sectors),
    }
