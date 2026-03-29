import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.title("🪙 Gold Price Prediction Dashboard")

# Path setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
file_path = os.path.join(ROOT_DIR, "outputs", "predictions.csv")

# Load data
if os.path.exists(file_path):
    data = pd.read_csv(file_path)

    # Fix alignment
    data = data.reset_index(drop=True)

    st.subheader("📊 Prediction vs Actual")

    # 🔥 MATPLOTLIB CHART
    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(data['Actual'].values, label='Actual')
    ax.plot(data['Predicted'].values, label='Predicted')

    ax.set_title("Gold Price Prediction")
    ax.set_xlabel("Data Points")
    ax.set_ylabel("Price")
    ax.legend()

    st.pyplot(fig)

else:
    st.error("❌ Run main.py first to generate predictions.csv")