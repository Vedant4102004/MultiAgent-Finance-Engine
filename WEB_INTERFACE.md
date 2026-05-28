# 💰 Web Interface Setup & Usage

## 🚀 Quick Start

### 1. Run the Web Application

```bash
cd ~/Desktop/MultiAgent_Finance_Debate_Engine
source venv/bin/activate
streamlit run web_app.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## 📋 Features

### 🏢 Single Stock Analysis
- Analyze any company
- View real-time market data
- Read latest news headlines
- Get AI-powered investment recommendation
- See Bull, Bear, and Risk perspectives

### 🎯 Portfolio Analysis
- Add multiple companies at once
- Compare holdings side-by-side
- View portfolio weights
- Calculate average returns and P/E ratios
- Analyze sector diversity
- Get individual recommendations for each stock

### 📊 Market Overview
- Preset portfolios (Tech Giants, Indian Leaders, Mixed)
- Custom portfolio creation
- Compare multiple companies
- Download portfolio data

---

## 📊 What You'll See

### Single Stock Analysis Output:
```
📊 Market Data
├── Current Price: $150.25
├── Market Cap: $2.5T
├── P/E Ratio: 28.5
└── 1Y Return: +15.3%

🐂 Bull Case
"Apple has strong fundamentals..."

🐻 Bear Case
"Concerns about valuation..."

⚠️ Risk Analysis
"Interest rate, regulatory risks..."

⚖️ Judge's Verdict
"Recommendation: BUY (85% confidence)"
```

### Portfolio Analysis Output:
```
📊 Portfolio Summary
├── 3 Companies
├── Avg Return: +12.5%
├── Avg P/E: 25.3
└── Sector Diversity: 2

💼 Holdings Table
├── Apple | $2.5T | 28.5 P/E
├── Microsoft | $2.4T | 32.1 P/E
└── Google | $1.8T | 24.7 P/E

⚖️ Portfolio Weights
├── Apple: 35%
├── Microsoft: 32%
└── Google: 33%
```

---

## 🎮 Navigation

**Left Sidebar:**
- Select analysis type
- Three options:
  1. 🏢 Single Stock Analysis
  2. 🎯 Portfolio Analysis
  3. 📊 Market Overview

---

## ⚙️ Configuration

### Market Data Sources
- **yfinance** - Stock prices, market cap, P/E ratios
- **Finnhub** - News headlines, company fundamentals

### Supported Companies
- US: Apple, Microsoft, Google, Amazon, Meta, Tesla, Netflix
- India: Reliance, Tata, Infosys, HCL, Wipro, ICICI, HDFC
- Add custom tickers in `tools/data_fetcher.py`

---

## 🔧 Customization

### Add New Companies
Edit `tools/data_fetcher.py`:
```python
ticker_map = {
    "reliance": "RELIANCE.NS",
    "your_company": "TICKER_HERE",  # Add here
}
```

### Add New Preset Portfolio
Edit `web_app.py`:
```python
preset_portfolios = {
    "Tech Giants": ["Apple", "Microsoft", "Google"],
    "My Portfolio": ["Apple", "Tesla", "Amazon"],  # Add here
}
```

### Change Model
Edit `.env`:
```
HF_MODEL_REPO=mistralai/Mistral-7B-Instruct-v0.2  # Change this
```

---

## 📊 Performance

- **First Load**: ~30-60 seconds (model loading)
- **Analysis**: ~15-30 seconds per company
- **Portfolio**: ~60-120 seconds for 3-5 companies

---

## ⚠️ Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution:**
```bash
source venv/bin/activate
pip install streamlit
```

### Issue: "No market data for [company]"
**Solution:**
- Check if company ticker is correct in `data_fetcher.py`
- Verify the company is publicly listed
- Try another company

### Issue: App running slow
**Solution:**
- First run loads the model (normal)
- Subsequent runs are faster
- Close other browser tabs

### Issue: News not showing
**Solution:**
- Add Finnhub API key to `.env`
- Check API rate limits (free tier: 60 calls/min)

---

## 📱 Tips & Tricks

1. **Bookmark favorite companies** - Use browser bookmarks
2. **Export data** - Copy table and paste to Excel
3. **Compare sectors** - Analyze multiple companies from same sector
4. **Track performance** - Bookmark recommendations and track accuracy

---

## 🚀 Next Steps

1. Run the app: `streamlit run web_app.py`
2. Start with Single Stock Analysis
3. Try Portfolio Analysis with 3-5 companies
4. Use Market Overview for sector analysis
5. Customize preset portfolios

---

**Enjoy your AI-powered investment analysis! 📈**
