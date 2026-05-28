from langchain.tools import tool
import requests
import os
from rich import print
import yfinance as yf
from dotenv import load_dotenv
load_dotenv()


@tool
def get_stock_data(ticker: str) -> str:
    """Get the stock details for a given ticker symbol."""
    stock =  yf.Ticker(ticker)
    data = stock.info

    return {
        "company": data.get("longName"),
        "current_price": data.get("currentPrice"),
        "market_cap": data.get("marketCap"),
        "pe_ratio": data.get("trailingPE"),
        "sector": data.get("sector"),
    }