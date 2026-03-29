# 🪙 Gold Price Prediction (XAUUSD)

A Machine Learning-based project to predict Gold prices (XAUUSD) using technical indicators and visualize results with an interactive dashboard.

---

## 🚀 Project Overview

This project uses historical gold price data along with technical indicators like **RSI, MACD, and Moving Averages** to train machine learning models and predict future prices.

It also includes a **Streamlit dashboard** to visualize predictions vs actual prices.

---

## 🎯 Features

* 📊 Gold price prediction using ML models
* 📈 Technical Indicators:

  * Moving Average (MA50)
  * RSI (Relative Strength Index)
  * MACD
* 🤖 Model Used:

  * Random Forest Regressor
* 📉 Prediction vs Actual comparison chart
* 🖥️ Interactive Streamlit Dashboard
* 💾 CSV export of predictions

---

## 🧠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* yfinance

---

## 📁 Project Structure

```
gold-price-prediction/
│
├── data/
├── outputs/
│   └── predictions.csv
│
├── src/
│   ├── data_loader.py
│   ├── indicators.py
│   ├── signals.py
│   ├── model.py
│   ├── train.py
│   └── predict.py
│
├── app/
│   └── app.py
│
├── main.py
└── requirements.txt
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/gold-price-prediction.git
cd gold-price-prediction
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
```

---

### 3️⃣ Activate Environment

**Windows (PowerShell):**

```
.\.venv\Scripts\Activate.ps1
```

If error occurs:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

---

### 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Step 1: Run ML Pipeline

```
python main.py
```

👉 This generates:

```
outputs/predictions.csv
```

---

### Step 2: Run Dashboard

```
streamlit run app/app.py
```

---

## 📊 Output

* 📈 Prediction vs Actual chart
* 📁 predictions.csv file
* 📊 Clean visualization using Matplotlib

---

## ⚠️ Common Errors & Fixes

### ❌ FileNotFoundError

👉 Run `main.py` before dashboard

---

### ❌ No module named matplotlib

```
pip install matplotlib
```

---

### ❌ PowerShell Execution Error

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

---

## 💡 Future Improvements

* 📊 Candlestick charts (TradingView style)
* 🟢 Buy/Sell signals visualization
* 💰 Backtesting system (profit, win rate)
* 🤖 Deep Learning (LSTM model)
* 📡 Live price integration

---

## 🧑‍💻 Author

**Ansh Suhagiya**

* Trader 📈
* IT Student 💻
* Machine Learning Enthusiast 🤖

---

## ⭐ Why This Project?

This project demonstrates:

* Real-world financial data handling
* Machine learning implementation
* Data visualization skills
* End-to-end project development

---

🔥 *This project is a strong portfolio piece for ML + Finance roles*
