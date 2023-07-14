# main.py
from sklearn.linear_model import LinearRegression

def main():
    # Training data
    X_train = [[1], [2], [3], [4], [5]]
    y_train = [2, 4, 6, 8, 10]

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Test the model
    X_test = [[6]]
    y_pred = model.predict(X_test)
    print("Prediction:", y_pred)

if __name__ == "__main__":
    main()
