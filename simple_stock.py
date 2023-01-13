import streamlit as st
import  yfinance as yf
import pandas as pd
st.write("""
# Simple Stock Price App

*Show are the stock closing price and Volume of TESLA*
""")
ticker_symbol="TSLA"
ticker_data=yf.Ticker(ticker_symbol)
tickerdf=ticker_data.history(period="1d",start="2010-6-15",end="2022-11-20")
st.write("""
# Closing Price
""")
st.line_chart(tickerdf.Close)
st.write("""
# Volume
""")
st.line_chart(tickerdf.Volume
              )
