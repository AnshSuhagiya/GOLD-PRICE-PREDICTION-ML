def generate_signals(data):
    signals = []

    for i in range(len(data)):
        if data['RSI'][i] < 30 and data['MACD'][i] > 0:
            signals.append("BUY")
        elif data['RSI'][i] > 70 and data['MACD'][i] < 0:
            signals.append("SELL")
        else:
            signals.append("HOLD")

    data['Signal'] = signals
    return data