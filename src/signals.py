def generate_signals(data):
    data['Signal'] = 'HOLD'
    data = data.reset_index(drop=True)

    for i in range(1, len(data)):
        rsi = data['RSI'].iloc[i]
        macd = data['MACD'].iloc[i]

        if rsi < 30 and macd > 0:
            data.loc[data.index[i], 'Signal'] = 'BUY'
        elif rsi > 70 and macd < 0:
            data.loc[data.index[i], 'Signal'] = 'SELL'

    return data


def backtest(data):
    data = data.reset_index(drop=True)
    balance = 10000.0
    position = 0.0

    for i in range(len(data)):
        signal = data['Signal'].iloc[i]
        price = float(data['Close'].iloc[i])

        if signal == 'BUY' and position == 0:
            position = balance / price
            balance = 0.0
        elif signal == 'SELL' and position > 0:
            balance = position * price
            position = 0.0

    final_value = balance if balance > 0 else position * float(data['Close'].iloc[-1])
    return final_value