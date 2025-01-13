# Stock Price Visualizer Tool

This Python project allows users to fetch stock price data, calculate moving averages, and visualize stock trends using the `yfinance` library.

## Features

- Fetch historical stock price data for any stock ticker symbol.
- Calculate short-term and long-term moving averages.
- Visualize stock prices along with moving averages in an interactive chart.

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
   pip install yfinance
   pip install pandas
   pip install matplotlib
   ```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. Enter the stock ticker symbol, start date, and end date when prompted.

Example:
```
Enter stocks Ticker symbol: AAPL
Enter start date (Year-MM-DD): 2023-01-01
Enter end date (Year-MM-DD): 2023-12-31
```

The program will fetch the data, calculate moving averages, and display a plot of the stock prices and moving averages.

## File Overview

- `main.py`: Main script for fetching, processing, and visualizing stock data.

## Example Output

After running the script, a plot will display the stock's closing prices and its 30-day and 100-day moving averages. The title of the chart will include the company's name and ticker symbol.

This project is licensed under the [MIT License](LICENSE).