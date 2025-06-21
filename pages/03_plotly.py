
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

# 🎯 시가총액 상위 10개 글로벌 기업 (2025년 기준 예상)
top10_companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Nvidia": "NVDA",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Berkshire Hathaway": "BRK-B",
    "Meta (Facebook)": "META",
    "Tesla": "TSLA",
    "TSMC": "TSM"
}

# 🧭 사이드바 설정
st.sidebar.title("📈 시가총액 Top 10 기업")
selected_companies = st.sidebar.multiselect("시각화할 기업 선택", list(top10_companies.keys()), default=list(top10_companies.keys()))

# 📆 날짜 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 📊 데이터 수집
def get_stock_data(ticker):
    data = yf.download(ticker, start=start_date, end=end_date)
    data["Company"] = ticker
    return data

st.title("🌍 글로벌 시가총액 Top 10 기업의 주가 변화 (최근 1년)")
st.caption("📊 데이터 출처: Yahoo Finance")

# 📈 Plotly 그래프 생성
fig = go.Figure()
for company in selected_companies:
    ticker = top10_companies[company]
    data = get_stock_data(ticker)
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name=company))

# ✨ 그래프 꾸미기
fig.update_layout(
    title="주가 변화 추이 (최근 1년)",
    xaxis_title="날짜",
    yaxis_title="종가 (USD)",
    template="plotly_white",
    height=600
)

st.plotly_chart(fig, use_container_width=True)
