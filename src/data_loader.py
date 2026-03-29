import yfinance as yf

# def load_data():
#     data = yf.download("GC=F", start="2015-01-01")
#     data.to_csv("Data/gold_data.csv")
#     return data

def load_data(symbol="GC=F", start="2015-01-01", save=False):

    """
    Fetch historical market data using Yahoo Finance.

    Parameters:
    symbol (str): Trading symbol (default: GC=F for gold)
    start (str): Start date in YYYY-MM-DD format
    save (bool): If True, saves data to CSV

    Returns:
    pandas.DataFrame: Historical OHLCV data
    """

    data = yf.download(symbol, start=start)

    if save:
        data.to_csv("data/gold_data.csv")

    return data