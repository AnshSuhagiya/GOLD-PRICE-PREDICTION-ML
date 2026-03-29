def add_indicators(data):
    data['MA50'] = data['Close'].rolling(50).mean()
    data['MA200'] = data['Close'].rolling(200).mean()
    data['Return'] = data['Close'].pct_change()
    data.dropna(inplace=True)
    return data