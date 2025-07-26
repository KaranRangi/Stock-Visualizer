import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def getStockData(ticker):
    try:
        data = yf.download(ticker, period="5y")
        if data.empty:
            print("Could not find any data for this ticker.")
            return None
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None

def prepareData(data):
    # Reset index to get date as a column
    data = data.reset_index()

    # Convert date to ordinal for regression (numerical representation)
    data['Date'] = pd.to_datetime(data['Date'])
    data['DateOrdinal'] = data['Date'].map(pd.Timestamp.toordinal)

    # Features and targets
    X = data[['DateOrdinal']]
    y = data[['Close']]

    return X, y, data

def trainAndPredict(X, y, futureDays=365):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict future dates
    last_date = X['DateOrdinal'].max()
    futureDates = np.array([last_date + i for i in range(1, futureDays + 1)]).reshape(-1, 1)
    predictions = model.predict(futureDates)

    return model, futureDates, predictions

def plotPredictions(data, X, y, futureDates, predictions, ticker):
    plt.figure(figsize=(14, 6))
    plt.plot(data['Date'], y, label='Historical Price')
    plt.plot([pd.Timestamp.fromordinal(int(d[0])) for d in futureDates], predictions, label='Predicted Price', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title(f'{ticker.upper()} Stock Price Prediction for Next Year')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def buyOrSellDecision(predictions):
    if predictions[-1] > predictions[0]:
        return "Prediction: Price expected to rise — You may consider BUYING."
    else:
        return "Prediction: Price expected to fall — You may consider SELLING."

if __name__ == "__main__":
    ticker = input("Enter stock ticker symbol: ").upper()
    data = getStockData(ticker)

    if data is not None:
        X, y, full_data = prepareData(data)
        model, futureDates, predictions = trainAndPredict(X, y)

        # Decision logic
        decision = buyOrSellDecision(predictions)
        print(decision)

        plotPredictions(full_data, X, y, futureDates, predictions, ticker)

