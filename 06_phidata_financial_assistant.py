"""
Phidata - Financial Data Analysis Assistant
============================================
Task-specific agents that excel at their particular domain.
Automated financial analysis with stock data.

Requirements:
- phidata
- yfinance
- pandas
- openai
- OpenAI API key

Author: AI Agents Article Examples
"""

import os
import yfinance as yf
import pandas as pd
from phidata.assistant import Assistant
from phidata.tools import FunctionTool
from phi.model.openai import OpenAIChat

# Define financial data functions
def get_stock_info(ticker: str) -> dict:
    """Get detailed stock information"""
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "company_name": info.get("shortName"),
        "current_price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("forwardPE"),
        "dividend_yield": info.get("dividendYield"),
        "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
        "fifty_two_week_low": info.get("fiftyTwoWeekLow")
    }

def compare_stocks(tickers: list) -> pd.DataFrame:
    """Compare multiple stocks side by side"""
    data = []
    for ticker in tickers:
        info = get_stock_info(ticker)
        info["ticker"] = ticker.upper()
        data.append(info)
    return pd.DataFrame(data)

def generate_analysis_report(stock_data: dict) -> str:
    """Generate investment analysis summary"""
    analysis = []
    for ticker, info in stock_data.items():
        pe = info.get("pe_ratio", 0)
        div = info.get("dividend_yield", 0)
        
        if pe and pe < 20:
            valuation = "potentially undervalued"
        elif pe and pe > 30:
            valuation = "potentially overvalued"
        else:
            valuation = "fairly valued"
        
        analysis.append(f"""
        {ticker.upper()} Analysis:
        - Current valuation appears {valuation}
        - P/E Ratio: {pe:.2f}
        - Dividend Yield: {(div * 100):.2f}% if div else "N/A"
        """)
    
    return "\n".join(analysis)

# Initialize the financial assistant
financial_assistant = Assistant(
    name="FinancialAnalyst",
    model=OpenAIChat(id="gpt-4"),
    description="I am a financial analysis assistant. I can fetch stock data, compare companies, and generate investment reports.",
    tools=[
        FunctionTool.from_function(get_stock_info),
        FunctionTool.from_function(compare_stocks),
        FunctionTool.from_function(generate_analysis_report)
    ],
    show_tool_calls=True
)

# Example analysis session
financial_assistant.print_response("""
Compare Apple (AAPL), Microsoft (MSFT), and Google (GOOGL).
Which company appears most attractively valued based on P/E ratio?
""")

financial_assistant.print_response("""
Generate a comprehensive investment report for Tesla (TSLA)
and include recommendations based on current metrics.
""")

if __name__ == "__main__":
    # How to run this code:
    # 1. pip install phidata yfinance pandas openai
    # 2. Set OPENAI_API_KEY environment variable
    # 3. Run: python 06_phidata_financial_assistant.py
    pass
