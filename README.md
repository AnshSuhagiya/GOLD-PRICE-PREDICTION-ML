# 📈 Gold Price Prediction using Machine Learning

This project focuses on predicting gold prices using historical data and machine learning techniques. It uses financial data along with technical indicators to train a regression model and generate predictions.

---

## 🚀 Features

* 📊 Fetches real-time historical gold price data using `yfinance`
* 📉 Adds technical indicators (Moving Averages, Returns)
* 🤖 Trains a Machine Learning model (Linear Regression)
* 📏 Evaluates model performance using Mean Squared Error (MSE)
* 🔮 Predicts future gold prices

---

## 🧠 Tech Stack

* Python
* pandas
* numpy
* scikit-learn
* yfinance

---

## 📁 Project Structure

```
project/
│
├── data/                  # Dataset storage (not pushed to GitHub)
│
├── src/
│   ├── data_loader.py     # Fetches data
│   ├── indicators.py      # Adds technical indicators
│   ├── model.py           # ML model
│   ├── train.py           # Training logic
│   └── predict.py         # Prediction logic
│
├── main.py                # Entry point
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── .gitignore             # Ignore unnecessary files
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/gold-price-prediction.git
cd gold-price-prediction
```

2. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the project:

```
python main.py
```

---

## 📊 How It Works

1. Data is fetched using Yahoo Finance API
2. Technical indicators like:

   * Moving Average (MA50, MA200)
   * Daily Returns
     are added
3. Data is split into training and testing sets
4. A Linear Regression model is trained
5. Predictions are made and evaluated using MSE

---

## 📉 Example Output

```
MSE: 123.45
```

---

## 🔧 Future Improvements

* Add advanced models (Random Forest, XGBoost)
* Hyperparameter tuning
* Add visualization (matplotlib, seaborn)
* Deploy as a web app (Flask/Streamlit)
* Add real-time prediction system

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* Yahoo Finance for financial data
* scikit-learn for ML tools

---

## 📬 Contact

If you have any questions or suggestions, feel free to reach out!

---
