import pandas as pd
import numpy as np
import os

from src.data_loader import load_data
from src.indicators import add_indicators
from src.signals import generate_signals, backtest
from src.model import get_model
from src.train import train_model
from src.predict import predict

# Create folders
os.makedirs("outputs", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Load fresh data from yfinance
data = load_data()

# Add technical indicators
data = add_indicators(data)

# Generate BUY/SELL signals
data = generate_signals(data)

# Drop any NaNs
data = data.dropna().reset_index(drop=True)

# Features and Target
X = data[['MA50', 'RSI', 'MACD']]
y = data['Close']

# Train ML model
model = get_model()
model, x_test, y_test = train_model(model, X, y)

# Predict
predictions = predict(model, x_test)

# Flatten arrays
y_test = np.ravel(y_test)
predictions = np.ravel(predictions)

# Save predictions
output = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})
output.to_csv("outputs/predictions.csv", index=False)

# Save full dataset with signals
data.to_csv("data/gold_data.csv", index=False)

# Backtest final balance
final_balance = backtest(data)

print("✅ DONE!")
print(f"💰 Final Balance: {final_balance:.2f}")