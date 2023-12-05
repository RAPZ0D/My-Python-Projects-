#Stocks Data
import requests
import psycopg2
from datetime import datetime

# Your Alpha Vantage API key
api_key = 'SJERGL47QPEJ09N3'

# Function to retrieve stock data from Alpha Vantage
def get_stock_data(symbol):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    stock_data = []
    if 'Time Series (Daily)' in data:
        time_series = data['Time Series (Daily)']
        for date, values in time_series.items():
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            stock_info = {
                'symbol': symbol,
                'date': date_obj.date(),
                'open': float(values['1. open']),
                'close': float(values['4. close']),
                'high': float(values['2. high']),
                'low': float(values['3. low']),
                'volume': int(values['5. volume'])
            }
            stock_data.append(stock_info)

    return stock_data

# Database connection details
db_params = {
    'host': 'localhost',
    'database': 'timeseriesanalysisdb',
    'user': 'postgres',
    'password': 'Duke#7539',
    'port': 5432
}

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object using the connection
    cursor = conn.cursor()

    # List of stock symbols: Apple, Microsoft, Tesla
    stock_symbols = ['AAPL', 'MSFT', 'TSLA']
    all_stock_data = []

    # Retrieve stock data for each symbol from Alpha Vantage
    for symbol in stock_symbols:
        stock_data = get_stock_data(symbol)
        all_stock_data.extend(stock_data)

    # Insert retrieved stock data into the 'stocks' table
    for stock_info in all_stock_data:
        cursor.execute("""
            INSERT INTO stocks (symbol, date, open, close, high, low, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (stock_info['symbol'], stock_info['date'], stock_info['open'], stock_info['close'],
                  stock_info['high'], stock_info['low'], stock_info['volume']))

    # Commit the changes and close cursor and connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Data successfully inserted into the 'stocks' table.")

except psycopg2.Error as e:
    print("Error connecting to the PostgreSQL database:", e)


# Technical_indicators
import requests
import psycopg2
from datetime import datetime

# Your Alpha Vantage API key
api_key = 'SJERGL47QPEJ09N3'

# Function to retrieve SMA and RSI from Alpha Vantage for a given symbol
def get_technical_indicators(symbol):
    base_url = 'https://www.alphavantage.co/query'
    params_sma = {
        'function': 'SMA',
        'symbol': symbol,
        'interval': 'daily',
        'time_period': '20',  # 20-day SMA
        'series_type': 'close',
        'apikey': api_key
    }

    response_sma = requests.get(base_url, params=params_sma)
    sma_data = response_sma.json()
    latest_sma_date = next(iter(sma_data.get('Technical Analysis: SMA', {}).keys()), None)
    latest_sma = next(iter(sma_data.get('Technical Analysis: SMA', {}).values()), {'SMA': None})['SMA']

    params_rsi = {
        'function': 'RSI',
        'symbol': symbol,
        'interval': 'daily',
        'time_period': '14',  # 14-day RSI
        'series_type': 'close',
        'apikey': api_key
    }

    response_rsi = requests.get(base_url, params=params_rsi)
    rsi_data = response_rsi.json()
    latest_rsi_date = next(iter(rsi_data.get('Technical Analysis: RSI', {}).keys()), None)
    latest_rsi = next(iter(rsi_data.get('Technical Analysis: RSI', {}).values()), {'RSI': None})['RSI']

    return {'symbol': symbol, 'date_sma': latest_sma_date, 'sma_20': latest_sma, 'date_rsi': latest_rsi_date, 'rsi': latest_rsi}

# List of stock symbols: Apple, Microsoft, Tesla
stock_symbols = ['AAPL', 'MSFT', 'TSLA']

# List to store technical indicators data
technical_indicators = []

# Retrieve SMA and RSI for each symbol
for symbol in stock_symbols:
    tech_indicators = get_technical_indicators(symbol)
    technical_indicators.append(tech_indicators)

# Database connection details
db_params = {
    'host': 'localhost',
    'database': 'timeseriesanalysisdb',
    'user': 'postgres',
    'password': 'Duke#7539',
    'port': 5432
}

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object using the connection
    cursor = conn.cursor()

    # Insert fetched data into the 'technical_indicators' table
    for tech_info in technical_indicators:
        cursor.execute("""
            INSERT INTO technical_indicators (symbol, date, sma_20, rsi, macd)
            VALUES (%s, COALESCE(%s, CURRENT_DATE), %s, %s, %s)
            """, (tech_info['symbol'], tech_info['date_sma'], tech_info['sma_20'], tech_info['rsi'], None))

    # Commit the changes and close cursor and connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Data successfully inserted into the 'technical_indicators' table.")

except psycopg2.Error as e:
    print("Error connecting to the PostgreSQL database:", e)

# New_sentiment_analysis 
import requests

# Your Alpha Vantage API key
api_key = 'SJERGL47QPEJ09N3'

# Function to get stock prices and dates
def get_stock_data(symbol):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key
    }

    response = requests.get(base_url, params=params)
    stock_data = response.json()

    if 'Time Series (Daily)' in stock_data:
        time_series = stock_data['Time Series (Daily)']
        prices_and_dates = [{'date': date, 'price': data['4. close']} for date, data in time_series.items()]
        return prices_and_dates

    return None

# List of stock symbols: Apple, Microsoft, Tesla
stock_symbols = ['AAPL', 'MSFT', 'TSLA']

# Dictionary to store stock prices and dates
stock_prices_dates = {}

# Retrieve stock prices and dates for each symbol
for symbol in stock_symbols:
    data = get_stock_data(symbol)
    stock_prices_dates[symbol] = data

# Displaying stock prices and dates
for symbol, data in stock_prices_dates.items():
    print(f"Stock Symbol: {symbol}")
    if data:
        for entry in data:
            print(f"Date: {entry['date']}, Price: {entry['price']}")
    else:
        print("No data available")

# Viaualization 
import psycopg2
import matplotlib.pyplot as plt

# Database connection details
db_params = {
    'host': 'localhost',
    'database': 'timeseriesanalysisdb',
    'user': 'postgres',
    'password': 'Duke#7539',
    'port': 5432
}

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object using the connection
    cursor = conn.cursor()

    # Fetch data from the 'stocks' table
    cursor.execute("SELECT date, close FROM stocks WHERE symbol = 'AAPL' ORDER BY date")
    data = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    conn.close()

    if data:
        # Separate the date and closing prices for plotting
        dates = [row[0] for row in data]
        closing_prices = [row[1] for row in data]

        # Create a simple line plot using Matplotlib
        plt.figure(figsize=(10, 6))
        plt.plot(dates, closing_prices, marker='o', linestyle='-')
        plt.title('AAPL Closing Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    else:
        print("No data available")

except psycopg2.Error as e:
    print("Error connecting to the PostgreSQL database:", e)

import psycopg2
import matplotlib.pyplot as plt

# Database connection details
db_params = {
    'host': 'localhost',
    'database': 'timeseriesanalysisdb',
    'user': 'postgres',
    'password': 'Duke#7539',
    'port': 5432
}

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object using the connection
    cursor = conn.cursor()

    # Fetch data for Apple (AAPL)
    cursor.execute("SELECT date, close FROM stocks WHERE symbol = 'AAPL' ORDER BY date")
    apple_data = cursor.fetchall()

    # Fetch data for Microsoft (MSFT)
    cursor.execute("SELECT date, close FROM stocks WHERE symbol = 'MSFT' ORDER BY date")
    microsoft_data = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    conn.close()

    if apple_data and microsoft_data:
        # Separate the date and closing prices for Apple
        apple_dates = [row[0] for row in apple_data]
        apple_closing_prices = [row[1] for row in apple_data]

        # Separate the date and closing prices for Microsoft
        microsoft_dates = [row[0] for row in microsoft_data]
        microsoft_closing_prices = [row[1] for row in microsoft_data]

        # Create a bar plot comparing Apple and Microsoft closing prices
        plt.figure(figsize=(10, 6))
        plt.bar(apple_dates, apple_closing_prices, width=0.4, align='center', label='AAPL', alpha=0.7)
        plt.bar(microsoft_dates, microsoft_closing_prices, width=0.4, align='edge', label='MSFT', alpha=0.7)
        plt.title('Comparison of AAPL and MSFT Closing Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

    else:
        print("No data available for either AAPL or MSFT")

except psycopg2.Error as e:
    print("Error connecting to the PostgreSQL database:", e)

