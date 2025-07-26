# Stock Price Predictor & Visualizer Tool

This Python project allows users to fetch historical stock price data using the `yfinance` library, train a simple linear regression model, and visualize both historical and predicted prices. It also offers a basic prediction on whether you may consider buying or selling based on future trends.

## Features

- Fetch historical stock data from Yahoo Finance (past 5 years).
- Train a Linear Regression model to predict stock prices for the next 365 days.
- Visualize historical and future predicted stock prices using `matplotlib`.
- Suggest a **buy or sell** decision based on future trend direction.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KaranRangi/Stock-Visualizer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Stock-Visualizer
   ```
3. Install the required dependencies:
   ```bash
   pip install yfinance pandas numpy matplotlib scikit-learn
   ```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. Enter the stock ticker symbol when prompted.

Example:
```
Enter stock ticker symbol: AAPL
```

The program will:
- Download 5 years of data for AAPL,
- Train a regression model,
- Predict prices for the next 365 days,
- Display a plot of historical and predicted prices,
- Output a recommendation to buy or sell.

## File Overview

- `main.py`: Main script for fetching data, training the model, making predictions, and visualizing the results.

## License

This project is licensed under the [MIT License](LICENSE).
