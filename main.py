import pandas as pd
import numpy as np
import os

from src.data_loader import load_data
from src.indicators import add_indicators
from src.signals import generate_signals
from src.model import get_model
from src.train import train_model
from src.predict import predict

# Ensure outputs folder exists
os.makedirs("outputs", exist_ok=True)

# Load data
data = load_data()

# Add indicators
data = add_indicators(data)

# Generate signals
data = generate_signals(data)

# Clean data
data = data.dropna()

# Features & Target
x = data[['MA50', 'RSI', 'MACD']]
y = data['Close']   # ✅ MUST be 1D

# Train model
model = get_model()
model, x_test, y_test = train_model(model, x, y)

# Predict
predictions = predict(model, x_test)

# ✅ FIx: convert to 1D
y_test = np.ravel(y_test)
predictions = np.ravel(predictions)

# Save output
output = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})

output.to_csv("outputs/predictions.csv", index=False)

print("✅ DONE! File saved in outputs/predictions.csv")