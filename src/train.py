from sklearn.model_selection import train_test_split
import numpy as np

def train_model(model, x, y):
    # ✅ FIx: ensure y is 1D
    y = np.ravel(y)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    model.fit(x_train, y_train)

    return model, x_test, y_test