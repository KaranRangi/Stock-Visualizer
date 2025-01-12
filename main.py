import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#Get stock data
def getStockData(ticker, sDate, eDate):
    try:
        data = yf.download(ticker, start=sDate, end=eDate)

        if data.empty:
            print("Count not find any data for the ticker or date range")
            return None
        
        return data
    
    except Exception as e:
        print(f"Error: {e}")
        return None

# Step 2: Calculate moving averages
def calculateMovingAverages(data, short_window=30, long_window=100):
    if data is None or data.empty: 
        print("Data is empty. Exiting.")
        return None

    data['Short_MA'] = data['Close'].rolling(window=short_window).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window).mean()
    return data

# Step 3: Plot the stock prices and moving averages
def plotStockData(data, ticker):

    stockInfo = yf.Ticker(ticker).info
    companyName = stockInfo.get("longName")

    plt.figure(figsize=(12,6))
    plt.plot(data['Close'], label=f'{ticker} Close Price')
    plt.plot(data['Short_MA'], label='Short MA (30 days)')
    plt.plot(data['Long_MA'], label='Long MA (100 days)')
    plt.title(f'{companyName} ({ticker}) Stock Prices with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

# Main function
if __name__ == "__main__":
    ticker = input("Enter stocks Ticker symbol: ")
    startDate = input("Enter start date (Year-MM-DD): ")
    endDate = input("Enter end date (Year-MM-DD): ")
    
    # Fetch the stock data
    stockData = getStockData(ticker, startDate, endDate)
    
    # Calculate the moving averages
    stockData = calculateMovingAverages(stockData)
    
    # Plot the data
    plotStockData(stockData, ticker)
