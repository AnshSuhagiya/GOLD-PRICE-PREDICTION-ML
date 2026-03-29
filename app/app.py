import streamlit as st
import pandas as pd
import os
import sys
import plotly.graph_objects as go

# Fix Python path to access src
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
sys.path.append(ROOT_DIR)

st.title("🪙 Gold Trading Dashboard")

# Load processed data
data_path = os.path.join(ROOT_DIR, "data", "gold_data.csv")
if not os.path.exists(data_path):
    st.error("❌ Run main.py first!")
    st.stop()

data = pd.read_csv(data_path)

# Ensure numeric
data['Close'] = pd.to_numeric(data['Close'], errors='coerce')

# Check signals exist
if 'Signal' not in data.columns:
    st.error("❌ Run main.py again!")
    st.stop()

data = data.dropna().reset_index(drop=True)

# Candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=data.index,
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close']
)])

# BUY signals
buy = data[data['Signal'] == 'BUY']
fig.add_trace(go.Scatter(
    x=buy.index,
    y=buy['Close'],
    mode='markers',
    name='BUY',
    marker=dict(symbol='triangle-up', size=10)
))

# SELL signals
sell = data[data['Signal'] == 'SELL']
fig.add_trace(go.Scatter(
    x=sell.index,
    y=sell['Close'],
    mode='markers',
    name='SELL',
    marker=dict(symbol='triangle-down', size=10)
))

st.plotly_chart(fig)

# Backtesting summary
st.subheader("💰 Backtesting Result")
initial = 10000.0
final = float(data['Close'].iloc[-1])
st.write(f"Initial Balance: ${initial:.2f}")
st.write(f"Final Price: ${final:.2f}")