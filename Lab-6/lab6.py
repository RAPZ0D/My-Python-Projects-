# 1 Data Retrival 
import yfinance as yf
import pandas as pd

def get_historical_stock_data(symbols, start_date, end_date):
    stock_data = pd.DataFrame()
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        stock_info = stock.history(start=start_date, end=end_date)
        if not stock_info.empty:
            stock_data[symbol] = stock_info['Close']
        else:
            print(f"No data available for {symbol}.")
    return stock_data

# List of stock symbols for five companies
company_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "FB"]

# Date range for the historical data
start_date = "2023-01-01"
end_date = "2023-10-31"

# Fetching historical stock data
historical_stock_data = get_historical_stock_data(company_symbols, start_date, end_date)

# Displaying the fetched data
print(historical_stock_data.head())

import yfinance as yf
import pandas as pd

def get_historical_stock_data(symbols, start_date, end_date):
    stock_data = pd.DataFrame()
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        stock_info = stock.history(start=start_date, end=end_date)
        if not stock_info.empty:
            stock_data[symbol] = stock_info['Close']
        else:
            print(f"No data available for {symbol}.")
    return stock_data

# List of stock symbols for five companies
company_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

# Date range for the historical data
start_date = "2023-01-01"
end_date = "2023-10-31"

# Fetching historical stock data
historical_stock_data = get_historical_stock_data(company_symbols, start_date, end_date)

# Save the DataFrame to a CSV file
csv_filename = "stock_data.csv"
historical_stock_data.to_csv(csv_filename)

print(f"Stock data saved to {csv_filename}")

df = pd.read_csv('stock_data.csv')
df.head()



# 2 Basic Analysis 
import yfinance as yf
import pandas as pd

def get_historical_stock_data(symbols, start_date, end_date):
    stock_data = pd.DataFrame()
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        stock_info = stock.history(start=start_date, end=end_date)
        if not stock_info.empty:
            stock_data[symbol] = stock_info['Close']
    return stock_data

symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
start_date = "2023-01-01"
end_date = "2023-10-31"

data = get_historical_stock_data(symbols, start_date, end_date)
returns = data.pct_change().dropna()

print(f"Average Daily Return:{returns.mean()}")

print(f"\nVolatility (Standard Deviation of Daily Return):\n{returns.std()}")

print(f"\nCorrelation between Stocks:\n{returns.corr()}")


# 3 Moving Average 
import yfinance as yf
import pandas as pd

# Function to fetch historical stock data for a single symbol
def get_historical_stock_data(symbol, start_date, end_date):
    stock = yf.Ticker(symbol)
    stock_info = stock.history(start=start_date, end=end_date)
    return stock_info

# Fetch historical stock data for a single stock (e.g., Apple Inc.)
stock_symbol = "AAPL"  # Example stock symbol
start_date = "2023-01-01"
end_date = "2023-10-31"

stock_data = get_historical_stock_data(stock_symbol, start_date, end_date)

# Calculate Simple Moving Average (SMA) for 50 days
sma_period = 50
stock_data['SMA'] = stock_data['Close'].rolling(window=sma_period).mean()

# Display the stock data with SMA
print(stock_data[['Close', 'SMA']])

import yfinance as yf
import pandas as pd

# Function to fetch historical stock data for a single symbol
def get_historical_stock_data(symbol, start_date, end_date):
    stock = yf.Ticker(symbol)
    stock_info = stock.history(start=start_date, end=end_date)
    return stock_info

# Fetch historical stock data for a single stock (e.g., Apple Inc.)
stock_symbol = "TSLA"  # Example stock symbol
start_date = "2023-01-01"
end_date = "2023-10-31"

stock_data = get_historical_stock_data(stock_symbol, start_date, end_date)

# Calculate Exponential Moving Average (EMA) for 20 days
ema_period = 20
stock_data['EMA'] = stock_data['Close'].ewm(span=ema_period, adjust=False).mean()

# Display the stock data with EMA
print(stock_data[['Close', 'EMA']])

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch historical stock data for a single symbol
def get_historical_stock_data(symbol, start_date, end_date):
    stock = yf.Ticker(symbol)
    stock_info = stock.history(start=start_date, end=end_date)
    return stock_info

# Fetch historical stock data for a single stock (e.g., Apple Inc.)
stock_symbol = "AAPL"  # Example stock symbol
start_date = "2022-01-01"
end_date = "2023-01-01"

stock_data = get_historical_stock_data(stock_symbol, start_date, end_date)

# Calculate Simple Moving Average (SMA) and Exponential Moving Average (EMA)
sma_period = 50
ema_period = 20
stock_data['SMA'] = stock_data['Close'].rolling(window=sma_period).mean()
stock_data['EMA'] = stock_data['Close'].ewm(span=ema_period, adjust=False).mean()

# Calculate Relative Strength Index (RSI)
delta = stock_data['Close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
average_gain = gain.rolling(window=14).mean()
average_loss = loss.rolling(window=14).mean()
rs = average_gain / average_loss
rsi = 100 - (100 / (1 + rs))
stock_data['RSI'] = rsi

# Plotting the data and indicators
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.plot(stock_data['SMA'], label=f'SMA ({sma_period} days)')
plt.plot(stock_data['EMA'], label=f'EMA ({ema_period} days)')
plt.title(f'{stock_symbol} Stock Analysis')
plt.legend()

# Identifying potential buy/sell points based on SMA, EMA, and RSI
buy_points = ((stock_data['SMA'] > stock_data['EMA']) & (stock_data['RSI'] < 30))
sell_points = ((stock_data['SMA'] < stock_data['EMA']) & (stock_data['RSI'] > 70))

plt.scatter(stock_data[buy_points].index, stock_data['Close'][buy_points], marker='^', color='g', label='Buy Signal')
plt.scatter(stock_data[sell_points].index, stock_data['Close'][sell_points], marker='v', color='r', label='Sell Signal')

plt.legend()
plt.show()


# 4 Portfolio Allocation 
import yfinance as yf
import pandas as pd
import numpy as np

# Function to fetch historical stock data for a single symbol
def get_historical_stock_data(symbol, start_date, end_date):
    stock = yf.Ticker(symbol)
    stock_info = stock.history(start=start_date, end=end_date)
    return stock_info['Close']

# Define the stocks and their respective allocation weights
stocks = {
    'AAPL': 0.4,
    'MSFT': 0.3,
    'GOOGL': 0.2,
    'AMZN': 0.1
}

# Date range for historical data
start_date = "2023-01-01"
end_date = "2023-10-31"

# Fetch historical stock data for the selected stocks
stock_closing_prices = pd.DataFrame()
for stock, weight in stocks.items():
    stock_closing_prices[stock] = get_historical_stock_data(stock, start_date, end_date)

# Calculate daily returns of the stocks
daily_returns = stock_closing_prices.pct_change().dropna()

# Calculate expected returns of individual stocks
expected_returns = daily_returns.mean() * 252  # Assuming 252 trading days in a year

# Calculate the covariance matrix
cov_matrix = daily_returns.cov() * 252  # Annualize covariance matrix

# Calculate portfolio expected return
portfolio_expected_return = np.sum(expected_returns * np.array(list(stocks.values())))

# Calculate portfolio risk (standard deviation)
weights = np.array(list(stocks.values()))
portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
portfolio_volatility = np.sqrt(portfolio_variance)

print("Expected returns of individual stocks:")
print(expected_returns)
print("\nPortfolio Expected Return:", portfolio_expected_return)
print("Portfolio Risk:", portfolio_volatility)


# 5 Risk Return Analysis
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to fetch historical stock data for a single symbol
def get_historical_stock_data(symbol, start_date, end_date):
    stock = yf.Ticker(symbol)
    stock_info = stock.history(start=start_date, end=end_date)
    return stock_info['Close']

# Define the stocks
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

# Date range for historical data
start_date = "2023-01-01"
end_date = "2023-10-31"

# Initialize lists to store returns and volatility for different stocks
stock_returns = []
stock_volatility = []

for stock in stocks:
    stock_prices = get_historical_stock_data(stock, start_date, end_date)
    daily_returns = stock_prices.pct_change().dropna()

    # Calculate expected return of the stock
    expected_return = daily_returns.mean() * 252  # Assuming 252 trading days in a year
    stock_returns.append(expected_return)

    # Calculate volatility (standard deviation) of the stock
    volatility = daily_returns.std() * np.sqrt(252)  # Annualized standard deviation
    stock_volatility.append(volatility)

# Plotting the risk-return profile for individual stocks
plt.figure(figsize=(10, 6))
for i, stock in enumerate(stocks):
    plt.scatter(stock_volatility[i], stock_returns[i], label=stock, s=100)

plt.title('Risk-Return Profile of Individual Stocks')
plt.xlabel('Volatility (Risk)')
plt.ylabel('Expected Return')
plt.legend()
plt.grid(True)
plt.show()

# 6 Performance Metrics 
import yfinance as yf
import pandas as pd
import numpy as np
from scipy import stats

# Function to fetch historical stock data for a single symbol
def get_historical_stock_data(symbol, start_date, end_date):
    stock = yf.Ticker(symbol)
    stock_info = stock.history(start=start_date, end=end_date)
    return stock_info['Close']

# Define the stocks and their respective allocation weights
stocks = {
    'AAPL': 0.3,
    'MSFT': 0.3,
    'GOOGL': 0.2,
    'AMZN': 0.2,
    'TSLA': 0.1 
}

# Date range for historical data
start_date = "2023-01-01"
end_date = "2023-10-31"

# Fetch historical stock data for the selected stocks
stock_closing_prices = pd.DataFrame()
for stock, weight in stocks.items():
    stock_closing_prices[stock] = get_historical_stock_data(stock, start_date, end_date)

# Calculate daily returns of the stocks
daily_returns = stock_closing_prices.pct_change().dropna()

# Calculate expected returns of individual stocks
expected_returns = daily_returns.mean() * 252  # Assuming 252 trading days in a year

# Calculate market return (e.g., S&P 500 or market proxy)
market_return = get_historical_stock_data('SPY', start_date, end_date).pct_change().dropna()

# Ensure market return and daily returns have the same length
# Trim or align the market return data to match the length of daily returns
market_return = market_return.tail(len(daily_returns))

# Calculate excess returns of portfolio over market return
excess_returns = expected_returns - market_return.mean() * 252

# Calculate CAPM Beta using linear regression
beta, alpha, _, _, _ = stats.linregress(market_return, daily_returns.mean(axis=1) - market_return)

# Assuming risk-free rate is 0 for this example
risk_free_rate = 0

# Calculate CAPM Expected Return
CAPM_expected_return = risk_free_rate + beta * (market_return.mean() * 252 - risk_free_rate)

# Calculate Jensen's Alpha
jensens_alpha = (expected_returns - CAPM_expected_return).sum()

# Calculate downside deviation (standard deviation of negative returns)
downside_returns = daily_returns.copy()
downside_returns[downside_returns > 0] = 0  # Set positive returns to 0
downside_deviation = np.sqrt((downside_returns ** 2).mean()) * np.sqrt(252)  # Annualize downside deviation

# Calculate Sortino Ratio
sortino_ratio = (expected_returns - 0) / downside_deviation  # Assume risk-free rate is 0

# Calculate portfolio expected return
portfolio_weights = np.array(list(stocks.values()))
portfolio_return = np.sum(expected_returns * portfolio_weights)

# Calculate portfolio risk (standard deviation)
portfolio_variance = np.dot(portfolio_weights.T, np.dot(daily_returns.cov() * 252, portfolio_weights))
portfolio_volatility = np.sqrt(portfolio_variance)

# Calculate Sharpe Ratio
sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility

# Output all metrics
print("Sharpe Ratio:", sharpe_ratio)
print("Sortino Ratio:", sortino_ratio.sum())
print("Jensen's Alpha:", jensens_alpha)

# 7 Visualizing and Reporting
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch historical stock data for a single symbol
def get_historical_stock_data(symbol, start_date, end_date):
    stock = yf.Ticker(symbol)
    stock_info = stock.history(start=start_date, end=end_date)
    return stock_info

# Define the stocks for the portfolio
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

# Date range for historical data
start_date = "2023-01-01"
end_date = "2023-10-31"

# Fetch historical stock data for the selected stocks
stock_data = {}
for stock in stocks:
    stock_data[stock] = get_historical_stock_data(stock, start_date, end_date)

# Plotting stock data - Adjust this part for each specific visualization needed
plt.figure(figsize=(12, 6))

# Plot stock closing prices
for stock, data in stock_data.items():
    plt.plot(data['Close'], label=stock)

plt.title('Stock Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# Calculate and print key financial metrics
print("\nKey Financial Metrics:")
for stock, data in stock_data.items():
    print(f"\n{stock}")
    print("Mean Close Price:", data['Close'].mean())
    print("Standard Deviation of Close Price:", data['Close'].std())
    print("Max Close Price:", data['Close'].max())
    print("Min Close Price:", data['Close'].min())

# 8 Investment Recommendation 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch historical stock data for a single symbol
def get_historical_stock_data(symbol, start_date, end_date):
    stock = yf.Ticker(symbol)
    stock_info = stock.history(start=start_date, end=end_date)
    return stock_info

# Define the stocks for the portfolio
stocks =  ['AAPL', 'TSLA', 'GOOGL', 'MSFT', 'AMZN', 'NVDA', 'INTC', 'CSCO', 'PYPL']

# Date range for historical data
start_date = "2023-01-01"
end_date = "2023-10-31"

# Fetch historical stock data for the selected stocks
stock_data = {}
for stock in stocks:
    stock_data[stock] = get_historical_stock_data(stock, start_date, end_date)

# Plotting stock data - Line chart
plt.figure(figsize=(12, 6))

# Plot stock closing prices
for stock, data in stock_data.items():
    plt.plot(data['Close'], label=stock)

plt.title('Stock Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# Generate simple recommendations based on visual analysis
for stock, data in stock_data.items():
    if data['Close'][-1] > data['Close'].mean():
        print(f"Consider investing in {stock} as it is showing an upward trend.")
    else:
        print(f"Exercise caution for {stock} as it is not exhibiting a consistent upward trend.")

import yfinance as yf
def screen_stocks(symbols):
    suggested_stocks = []
    for symbol in symbols:
        hist_last_month = yf.download(symbol, period='1mo')
        if not hist_last_month.empty:
            if hist_last_month['Close'].iloc[0] < hist_last_month['Close'].iloc[-1]:
                suggested_stocks.append(symbol)
    
    return suggested_stocks
nasdaq_symbols = ['AAPL', 'TSLA', 'GOOGL', 'MSFT', 'AMZN', 'NVDA', 'INTC', 'CSCO', 'PYPL']
potential_stocks = screen_stocks(nasdaq_symbols)
print("Suggested Stocks based on Price Trend within the Last Month:")
print(potential_stocks)

