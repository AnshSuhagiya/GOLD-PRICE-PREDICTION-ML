from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_model(model, x, y):
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)

    print("MSE:", mse)

    return model, x_test, y_test