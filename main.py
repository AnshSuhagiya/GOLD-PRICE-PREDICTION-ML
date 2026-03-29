from src.data_loader import load_data
from src.indicators import add_indicators
from src.model import get_model
from src.train import train_model

def main():
    data = load_data()
    data = add_indicators(data)

    X = data[['MA50']]
    y = data['Close']

    model = get_model()
    model, x_test, y_test = train_model(model, X, y)

if __name__ == "__main__":
    main()