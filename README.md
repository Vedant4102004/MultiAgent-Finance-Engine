# 💰 Multi-Agent Finance Debate Engine

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.0+-green.svg)](https://www.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39.0+-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **AI-powered investment analysis engine using multi-agent debate system to provide balanced, data-driven investment recommendations**

## 🎯 Overview

The Multi-Agent Finance Debate Engine is an innovative AI system that analyzes investment opportunities through a structured debate framework. Instead of providing a single analysis, it simulates a real investment committee where:

- **🐂 Bull Agent** argues for investment (bullish perspective)
- **🐻 Bear Agent** argues against investment (bearish perspective)  
- **⚠️ Risk Analyst** identifies macro and external risks
- **⚖️ Judge Agent** synthesizes all perspectives into a final recommendation

Each agent is powered by **Mistral-7B LLM** and equipped with real-time market data, news, and financial fundamentals to make informed arguments.

---

## ✨ Features

### 🏢 Core Investment Analysis
- **Multi-agent debate system** - 4 specialized AI agents debate each investment
- **Real-time market data** - Live stock prices, P/E ratios, market caps via yfinance
- **News integration** - Latest headlines via Finnhub API
- **Company fundamentals** - Debt/equity, ROE, profit margins, sector data
- **Balanced recommendations** - BUY/HOLD/SELL with confidence levels (0-100%)

### 🎯 Portfolio Analysis
- **Multi-stock comparison** - Analyze entire portfolios at once
- **Portfolio weighting** - Calculate position sizes based on market cap
- **Sector diversity** - Understand sector allocation
- **Performance metrics** - Average returns, P/E ratios, comparative analysis
- **Individual recommendations** - Each stock analyzed separately within portfolio context

### 🌐 Web Interface
- **Streamlit-powered UI** - Beautiful, responsive web dashboard
- **Three analysis modes**:
  - 🏢 Single Stock Analysis
  - 🎯 Portfolio Analysis  
  - 📊 Market Overview with presets
- **Interactive visualizations** - Charts and tables for easy understanding
- **Real-time data** - Updates with latest market information

### 🔬 Advanced Features
- **RAG Integration** - Retrieval-Augmented Generation for document analysis
- **Dynamic company lookup** - Support for any publicly listed company
- **Graceful fallback** - Works even with limited/missing data
- **Comprehensive logging** - Track all analyses and recommendations

---

## 🏗️ Architecture

### System Design
```
┌─────────────────────────────────────────────────────┐
│         Web Interface (Streamlit)                   │
│  ┌──────────────────────────────────────────────┐   │
│  │ Single Stock │ Portfolio │ Market Overview  │   │
│  └──────────────────────────────────────────────┘   │
└──────────────┬──────────────────────────────────────┘
               │
┌──────────────▼──────────────────────────────────────┐
│         Data Fetcher Layer                          │
│  ┌──────────────┐  ┌──────────────┐                │
│  │  yfinance    │  │  Finnhub API │                │
│  │ (Real-time)  │  │   (News)     │                │
│  └──────────────┘  └──────────────┘                │
└──────────────┬──────────────────────────────────────┘
               │
┌──────────────▼──────────────────────────────────────┐
│      Multi-Agent Debate System                      │
│  ┌────────────┬──────────┬──────────┬──────────┐   │
│  │ Bull Agent │Bear Agent│Risk Agent│Judge Agt │   │
│  │(Mistral-7B)└──────────┴──────────┴──────────┘   │
│  │    All powered by LangChain Core                │
│  └──────────────────────────────────────────────┘   │
└──────────────┬──────────────────────────────────────┘
               │
┌──────────────▼──────────────────────────────────────┐
│      Portfolio Analyzer                            │
│  - Weight calculations                             │
│  - Sector analysis                                 │
│  - Performance metrics                             │
└─────────────────────────────────────────────────────┘
```

### Agent Roles

#### 🐂 Bull Agent (Bullish Perspective)
- Arguments for investment
- Highlights growth opportunities
- Emphasizes positive fundamentals
- Considers market tailwinds
- Uses: Market data, news, company info

#### 🐻 Bear Agent (Bearish Perspective)
- Arguments against investment
- Identifies valuation concerns
- Highlights competitive risks
- Notes market headwinds
- Uses: Market data, news, company info

#### ⚠️ Risk Analyst (Risk Assessment)
- Identifies external risks:
  - Macroeconomic risks
  - Regulatory risks
  - Geopolitical risks
  - Industry-specific risks
- Does NOT duplicate bull/bear arguments
- Focuses purely on risk factors

#### ⚖️ Judge Agent (Final Verdict)
- Synthesizes all perspectives
- Weighs risks vs rewards
- Provides final recommendation
- Assigns confidence level (0-100%)
- Format: `[RECOMMENDATION] (Confidence%) - Reason`

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)
- 4GB+ RAM
- Internet connection for API calls

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/Vedant4102004/MultiAgent-Finance-Engine.git
cd MultiAgent-Finance-Engine
```

**2. Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure API keys**
```bash
# Create/edit .env file
nano .env

# Add:
HF_MODEL_REPO=mistralai/Mistral-7B-Instruct-v0.2
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
FINNHUB_API_KEY=your_finnhub_key_here
```

**5. Run the web interface**
```bash
streamlit run web_app.py
```

Browser opens at: `http://localhost:8501` 🎉

---

## 💻 Usage

### Web Interface (Recommended)

#### Single Stock Analysis
```
1. Open http://localhost:8501
2. Select "🏢 Single Stock Analysis"
3. Enter company name (e.g., "Apple", "Reliance", "Microsoft")
4. Click "🚀 Analyze"
5. View results:
   - 📊 Market data
   - 📰 Latest news
   - 🐂 Bull case
   - 🐻 Bear case
   - ⚠️ Risk analysis
   - ⚖️ Final verdict
```

#### Portfolio Analysis
```
1. Select "🎯 Portfolio Analysis"
2. Enter multiple companies (one per line):
   Apple
   Microsoft
   Google
3. Click "📈 Analyze Portfolio"
4. View:
   - Portfolio summary metrics
   - Holdings table
   - Portfolio weights (pie chart)
   - Individual stock recommendations
```

#### Market Overview
```
1. Select "📊 Market Overview"
2. Choose preset portfolio or create custom
3. Compare multiple companies at once
4. Download data if needed
```

### Command Line Interface

**Single company analysis:**
```bash
source venv/bin/activate
python app.py
# Enter: Apple
# Get recommendation
```

**For developers:**
```python
from app import run

result = run("Should I invest in Apple?", "Apple")
print(result)

# Output:
# Recommendation: BUY
# Confidence: 85%
# Reason: Apple's consistent growth, undervalued P/E ratio...
```

---

## �� Example Results

### Single Stock: Apple
```
📊 MARKET DATA FOR AAPL:
- Current Price: $310.85
- Market Cap: $4.57T
- P/E Ratio: 37.63
- 1Y Return: +55.71%
- Sector: Technology
- Debt to Equity: 79.55

🐂 Bull Case:
"Strong 1-year return of 55.71% outperforms market.
High market cap demonstrates influence. MacBook Neo
launch showing strong demand. AI leadership position."

🐻 Bear Case:
"High P/E ratio at 37.63 suggests overvaluation.
Debt-to-equity at 79.55 indicates leverage concerns.
Return on equity only 1.41% raises profitability questions."

⚠️ Risk Analysis:
"Interest rate risk from Fed policy. Regulatory risks
in multiple jurisdictions. Competition from Android.
Supply chain disruptions. Geopolitical tensions."

⚖️ Judge's Verdict:
Recommendation: BUY
Confidence: 85%
Reason: Rewards outweigh risks. Strong fundamentals,
market position, and innovation pipeline support
investment despite valuation concerns.
```

### Portfolio: Tech Giants
```
📊 PORTFOLIO SUMMARY:
├── 3 Companies
├── Avg Return: +45.2%
├── Avg P/E: 32.5
└── Sector Diversity: 1

💼 HOLDINGS:
Apple     $4.57T    37.63 P/E   Technology
Microsoft $2.80T    28.42 P/E   Technology
Google    $1.80T    24.71 P/E   Technology

⚖️ WEIGHTS:
Apple:     43.2%
Microsoft: 33.4%
Google:    23.4%
```

---

## 🔧 Configuration

### API Keys Setup

#### Hugging Face (LLM)
1. Go to https://huggingface.co/settings/tokens
2. Create new token (read access)
3. Add to `.env`:
```
HUGGINGFACEHUB_API_TOKEN=hf_xxxxxxxxxxxx
```

#### Finnhub (Market News)
1. Go to https://finnhub.io/
2. Sign up (free tier available)
3. Get API key from dashboard
4. Add to `.env`:
```
FINNHUB_API_KEY=d8brifhr01qkc5gd6h9gxxx
```

### Customize Company Tickers

Edit `tools/data_fetcher.py`:
```python
ticker_map = {
    "reliance": "RELIANCE.NS",      # NSE (India)
    "tata": "TATA.NS",               # NSE
    "apple": "AAPL",                 # NASDAQ
    "microsoft": "MSFT",             # NASDAQ
    "your_company": "YOUR_TICKER",   # Add here!
}
```

### Change LLM Model

Edit `.env`:
```
HF_MODEL_REPO=mistralai/Mistral-7B-Instruct-v0.2  # Current
HF_MODEL_REPO=meta-llama/Llama-2-7b-hf            # Alternative
HF_MODEL_REPO=tiiuae/falcon-7b-instruct           # Alternative
```

### Portfolio Presets

Edit `web_app.py`:
```python
preset_portfolios = {
    "Tech Giants": ["Apple", "Microsoft", "Google"],
    "Indian Leaders": ["Reliance", "Tata", "Infosys"],
    "My Portfolio": ["AAPL", "RELIANCE.NS"],  # Add here!
}
```

---

## 📦 Dependencies

### Core
- **LangChain** (0.3.0+) - AI framework, prompt templates
- **Mistral-7B** - Language model via Hugging Face
- **LangGraph** - Multi-agent orchestration

### Data & APIs
- **yfinance** (0.2.54+) - Real-time stock data
- **Finnhub** - News and company fundamentals
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing

### Vector/Embeddings
- **ChromaDB** (0.5.5+) - Vector database for RAG
- **FAISS** (1.8.0+) - Fast similarity search
- **Sentence-Transformers** (3.0.0+) - Embeddings

### Web Interface
- **Streamlit** (1.39.0+) - Web UI
- **FastAPI** (0.115.0+) - API framework (optional)

### ML/Hardware
- **Transformers** (4.45.0+) - Model loading
- **Torch** (2.4.0+) - ML framework
- **bitsandbytes** - Model quantization

Full list in `requirements.txt`

---

## 📂 Project Structure

```
MultiAgent-Finance-Engine/
├── agents/                    # AI agents
│   ├── bull_agent.py         # Bullish perspective
│   ├── bear_agent.py         # Bearish perspective
│   ├── risk_agent.py         # Risk analysis
│   └── judge_agent.py        # Final verdict
│
├── tools/                     # Utility tools
│   ├── data_fetcher.py       # Market data integration
│   ├── portfolio_analyzer.py # Portfolio analysis
│   ├── rag_tool.py           # RAG retrieval
│   └── market_tool.py        # Market utilities
│
├── rag/                       # RAG system
│   ├── loader.py             # Document loading
│   ├── chunker.py            # Text chunking
│   ├── vector_store.py       # Vector database
│   └── build_rag.py          # RAG orchestration
│
├── models/                    # LLM utilities
│   └── load_models.py        # Model loading
│
├── web_app.py                 # Streamlit interface
├── app.py                     # CLI interface
├── run.py                     # Main runner
├── requirements.txt           # Dependencies
├── .env                       # Configuration
├── README.md                  # This file
└── RUN_INSTRUCTIONS.txt       # Quick start guide
```

---

## 🎮 Advanced Usage

### Programmatic API

```python
from app import run

# Single analysis
result = run("Should I invest in Apple?", "Apple")
print(result)

# Portfolio analysis
from tools.portfolio_analyzer import analyze_portfolio

companies = ["Apple", "Microsoft", "Google"]
portfolio = analyze_portfolio(companies)
print(portfolio["portfolio_data"])  # DataFrame
```

### Custom Prompts

Edit agent files to customize arguments:

```python
# agents/bull_agent.py
prompt = ChatPromptTemplate.from_template("""
You are a bullish analyst focusing on [CUSTOM ANGLE]
Your job is to argue [CUSTOM ARGUMENT]
Use: [CUSTOM DATA SOURCES]
Now provide: [CUSTOM PERSPECTIVE]
""")
```

### Add New Data Sources

```python
# tools/data_fetcher.py
def get_custom_data(company):
    # Call your API
    return processed_data

# Then use in agents:
market_data = format_market_data(company)
custom_data = get_custom_data(company)
# Combine both
```

---

## ⚙️ Performance Tuning

### First Run (~60 seconds)
- Model download and loading
- Vector database initialization
- Normal - happens once

### Subsequent Runs (~30 seconds per company)
- Market data fetch
- News retrieval
- AI analysis
- Standard expected time

### Optimization Tips
```bash
# Use CPU quantization (faster, lower quality)
# Edit .env:
USE_QUANTIZATION=true

# Batch multiple analyses
# Reduce API calls
# Cache results locally
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue: "No module named 'streamlit'"**
```bash
source venv/bin/activate
pip install streamlit
```

**Issue: "No market data for [company]"**
- Verify company ticker in `data_fetcher.py`
- Check if company is publicly listed
- Try official ticker symbol (e.g., RELIANCE.NS for NSE)

**Issue: "Finnhub API Error 403"**
- Verify FINNHUB_API_KEY in .env
- Check API rate limits (60 calls/min on free tier)
- Wait a moment and retry

**Issue: App running very slow**
- First run: normal (model loading)
- Subsequent runs: should be faster
- Check internet speed
- Reduce portfolio size

**Issue: LLM not found**
- Verify HuggingFace token is correct
- Check internet connection
- Ensure HF_MODEL_REPO is set correctly

---

## 📈 Results Interpretation

### Recommendation Levels
- **BUY (90-100% confidence)**: Strong investment opportunity
- **BUY (70-89% confidence)**: Good opportunity with some concerns
- **HOLD (50-69% confidence)**: Mixed signals, wait for more data
- **HOLD (40-49% confidence)**: Concerns outweigh benefits
- **SELL (0-39% confidence)**: Significant risks, avoid

### Key Metrics to Watch
- **P/E Ratio**: <20 = undervalued, >30 = expensive
- **Debt/Equity**: <1 = healthy, >2 = risky leverage
- **ROE**: >15% = good, <5% = concerning
- **1Y Return**: >20% = strong, <0% = underperforming

---

## 🤝 Contributing

Contributions welcome! Areas to improve:

1. **New Data Sources**
   - Add earnings data
   - Include analyst ratings
   - Integrate insider trading info

2. **Agent Improvements**
   - Add ESG analysis agent
   - Add technical analysis agent
   - Add sentiment analysis agent

3. **UI Enhancements**
   - Export to PDF reports
   - Email alerts
   - Watchlist functionality

4. **Performance**
   - Caching layer
   - Batch analysis
   - Result persistence

### Development Setup
```bash
git clone <repo>
cd MultiAgent-Finance-Engine
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Make changes
git push origin feature/your-feature
```

---

## 📜 License

MIT License - See LICENSE file for details

---

## ⚠️ Disclaimer

**This is an educational tool, not financial advice.**

- Recommendations are AI-generated analysis only
- Always conduct your own research
- Consult with financial advisors before investing
- Past performance ≠ future results
- No guarantees of accuracy or completeness
- Use at your own risk

---

⭐ If this project helps you, please star it! 

