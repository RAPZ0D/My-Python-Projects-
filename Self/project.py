# ALPHA VANTAGE API
import requests
import json
import mysql.connector

# Your API key and stock symbols
api_key = "A7XLMMXWDS57GYAH"
symbols = ["AAPL", "TSLA", "MSFT"]
base_url = "https://www.alphavantage.co/query"

# MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# Establish a connection to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Create the 'stocks' table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stocks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        symbol VARCHAR(10),
        date DATE,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume BIGINT
    )
""")

# Iterate through symbols and retrieve data
for symbol in symbols:
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        time_series_data = data.get("Time Series (Daily)")

        for date, values in time_series_data.items():
            stock_date = date
            stock_open = values["1. open"]
            stock_high = values["2. high"]
            stock_low = values["3. low"]
            stock_close = values["4. close"]
            stock_volume = values["5. volume"]

            # SQL query to insert data into the 'stocks' table
            sql = "INSERT INTO stocks (symbol, date, open, high, low, close, volume) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (symbol, stock_date, stock_open, stock_high, stock_low, stock_close, stock_volume)

            # Execute the SQL query
            cursor.execute(sql, val)

            # Commit the changes to the database
            conn.commit()

    else:
        print(f"Failed to fetch data for {symbol}. Error {response.status_code}")

# Close the cursor and database connection
cursor.close()
conn.close()

### New Stocks 
import requests
import mysql.connector

api_key = "A7XLMMXWDS57GYAH"
symbols = ["GOOGL", "IBM", "NVDA"]
base_url = "https://www.alphavantage.co/query"

# MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# Establish a connection to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Create the 'newstocks' table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS newstocks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        symbol VARCHAR(10),
        date DATE,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume BIGINT
    )
""")

# Iterate through symbols and retrieve data
insert_success = False  # Flag to check if insertion is successful

for symbol in symbols:
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        time_series_data = data.get("Time Series (Daily)")

        for date, values in time_series_data.items():
            stock_date = date
            stock_open = values["1. open"]
            stock_high = values["2. high"]
            stock_low = values["3. low"]
            stock_close = values["4. close"]
            stock_volume = values["5. volume"]

            # SQL query to insert data into the 'newstocks' table
            sql = "INSERT INTO newstocks (symbol, date, open, high, low, close, volume) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (symbol, stock_date, stock_open, stock_high, stock_low, stock_close, stock_volume)

            # Execute the SQL query
            cursor.execute(sql, val)

            # Commit the changes to the database
            conn.commit()

        insert_success = True  # Set flag to True if data insertion is successful
    else:
        print(f"Failed to fetch data for {symbol}. Error {response.status_code}")

# Close the cursor and database connection
cursor.close()
conn.close()

if insert_success:
    print("Data stored successfully")

# Visualization 
import mysql.connector
import matplotlib.pyplot as plt

# MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# Establish a connection to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Fetch data from the 'stocks' table for Apple, Microsoft, and Tesla
symbols = ['AAPL', 'MSFT', 'TSLA']
data = {}

for symbol in symbols:
    query = f"SELECT date, open, close FROM stocks WHERE symbol = '{symbol}'"
    cursor.execute(query)
    result = cursor.fetchall()
    data[symbol] = {'date': [], 'open': [], 'close': []}
    for row in result:
        data[symbol]['date'].append(row[0])
        data[symbol]['open'].append(row[1])
        data[symbol]['close'].append(row[2])

# Close the cursor and database connection
cursor.close()
conn.close()

# Plotting the data
plt.figure(figsize=(10, 6))

for symbol in symbols:
    plt.plot(data[symbol]['date'], data[symbol]['open'], label=f'{symbol} Open', linestyle='-', marker='o')
    plt.plot(data[symbol]['date'], data[symbol]['close'], label=f'{symbol} Close', linestyle='-', marker='o')

plt.title('Stock Prices: Open vs Close')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2 
import mysql.connector
import matplotlib.pyplot as plt

# MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# Establish a connection to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Fetch data for maximum volume and corresponding date for each stock
symbols = ['AAPL', 'MSFT', 'TSLA']
max_volume_data = {}

for symbol in symbols:
    query = f"SELECT date, volume FROM stocks WHERE symbol = '{symbol}' ORDER BY volume DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        max_volume_data[symbol] = {'date': result[0], 'volume': result[1]}

# Close the cursor and database connection
cursor.close()
conn.close()

# Plotting the data as a pie chart
labels = [f"{symbol}\nDate: {max_volume_data[symbol]['date']}" for symbol in max_volume_data]
sizes = [max_volume_data[symbol]['volume'] for symbol in max_volume_data]
explode = (0.1, 0.1, 0.1)  # To explode the slices

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Maximum Volume for Stocks')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.legend(loc="best", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

#3 
import mysql.connector
import matplotlib.pyplot as plt

# MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# Establish a connection to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Fetch high values for Apple, Microsoft, and Tesla
symbols = ['AAPL', 'MSFT', 'TSLA']
data = {}

for symbol in symbols:
    query = f"SELECT date, high FROM stocks WHERE symbol = '{symbol}'"
    cursor.execute(query)
    result = cursor.fetchall()
    data[symbol] = {'date': [], 'high': []}
    for row in result:
        data[symbol]['date'].append(row[0])
        data[symbol]['high'].append(row[1])

# Close the cursor and database connection
cursor.close()
conn.close()

# Plotting the data as an area chart
plt.figure(figsize=(12, 6))

for symbol in symbols:
    if symbol == 'AAPL':
        plt.fill_between(data[symbol]['date'], data[symbol]['high'], label=symbol, alpha=0.5, color='orange')
    else:
        plt.fill_between(data[symbol]['date'], data[symbol]['high'], label=symbol, alpha=0.5)

plt.title('Comparison of High Prices for Stocks')
plt.xlabel('Date')
plt.ylabel('High Price')
plt.legend(loc='upper left')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#4 
import mysql.connector
import matplotlib.pyplot as plt

# MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# Establish a connection to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Fetch low values for Apple, Microsoft, and Tesla
symbols = ['AAPL', 'MSFT', 'TSLA']
data = {}

for symbol in symbols:
    query = f"SELECT date, low FROM stocks WHERE symbol = '{symbol}'"
    cursor.execute(query)
    result = cursor.fetchall()
    data[symbol] = {'date': [], 'low': []}
    for row in result:
        data[symbol]['date'].append(row[0])
        data[symbol]['low'].append(row[1])

# Close the cursor and database connection
cursor.close()
conn.close()

# Plotting the data as an area chart
plt.figure(figsize=(12, 6))

for symbol in symbols:
    if symbol == 'AAPL':
        plt.fill_between(data[symbol]['date'], data[symbol]['low'], label=symbol, alpha=0.5, color='gold')
    elif symbol == 'MSFT':
        plt.fill_between(data[symbol]['date'], data[symbol]['low'], label=symbol, alpha=0.5, color='red')
    elif symbol == 'TSLA':
        plt.fill_between(data[symbol]['date'], data[symbol]['low'], label=symbol, alpha=0.3, color='blue')

plt.title('Comparison of Low Prices for Stocks')
plt.xlabel('Date')
plt.ylabel('Low Price')
plt.legend(loc='upper left')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Displaying the rows and columns 
import mysql.connector
import pandas as pd

# MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# Establish a connection to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Fetch all rows from the stocks table
query = "SELECT * FROM stocks"
cursor.execute(query)
rows = cursor.fetchall()

# Get column names
columns = [desc[0] for desc in cursor.description]

# Close the cursor and database connection
cursor.close()
conn.close()

# Create a Pandas DataFrame for displaying the data
df = pd.DataFrame(rows, columns=columns)

# Display the DataFrame
print(df)

# New stock table display 
import pandas as pd
from sqlalchemy import create_engine

# MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# Create a SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

# Fetching data from the 'newstocks' table using Pandas and SQLAlchemy engine
query = "SELECT * FROM newstocks"
df = pd.read_sql(query, engine)

# Display the DataFrame
print(df)

#Visualizaiton New 
import mysql.connector
import matplotlib.pyplot as plt

# MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# Establish a connection to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Fetching data from the 'newstocks' table
symbols = ['GOOGL', 'IBM', 'NVDA']  # Assuming the symbols are GOOGL for Google, IBM, and NVDA for Nvidia
data = {}

for symbol in symbols:
    query = f"SELECT date, open FROM newstocks WHERE symbol = '{symbol}'"
    cursor.execute(query)
    result = cursor.fetchall()
    data[symbol] = {'date': [], 'open': []}
    for row in result:
        data[symbol]['date'].append(row[0])
        data[symbol]['open'].append(row[1])

# Close the cursor and database connection
cursor.close()
conn.close()

# Plotting the data as a line plot
plt.figure(figsize=(10, 6))

for symbol in symbols:
    plt.plot(data[symbol]['date'], data[symbol]['open'], label=symbol)

plt.title('Stock Open Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#2 
import mysql.connector
import matplotlib.pyplot as plt

# MySQL database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# Establish a connection to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Fetching data from the 'newstocks' table
symbols = ['GOOGL', 'IBM', 'NVDA']  # Assuming the symbols are GOOGL for Google, IBM, and NVDA for Nvidia
data = {}

for symbol in symbols:
    query = f"SELECT date, open FROM newstocks WHERE symbol = '{symbol}'"
    cursor.execute(query)
    result = cursor.fetchall()
    data[symbol] = {'date': [], 'open': []}
    for row in result:
        data[symbol]['date'].append(row[0])
        data[symbol]['open'].append(row[1])

# Close the cursor and database connection
cursor.close()
conn.close()

# Plotting the data as a line plot
plt.figure(figsize=(10, 6))

for symbol in symbols:
    plt.plot(data[symbol]['date'], data[symbol]['open'], label=symbol)

# Find and annotate highest and lowest points
for symbol in symbols:
    highest_point = max(data[symbol]['open'])
    lowest_point = min(data[symbol]['open'])
    date_highest = data[symbol]['date'][data[symbol]['open'].index(highest_point)]
    date_lowest = data[symbol]['date'][data[symbol]['open'].index(lowest_point)]
    
    plt.scatter(date_highest, highest_point, marker='o', color='green', label='Highest')
    plt.scatter(date_lowest, lowest_point, marker='o', color='red', label='Lowest')
    
    plt.text(date_highest, highest_point, f'{highest_point}', ha='right', va='bottom', fontsize=8)
    plt.text(date_lowest, lowest_point, f'{lowest_point}', ha='right', va='bottom', fontsize=8)

plt.title('Stock Open Prices with Highest and Lowest Points')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Final Visualization Combined tables
import mysql.connector
import matplotlib.pyplot as plt

# MySQL database connection details for 'stocks' table
db_config_stocks = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# MySQL database connection details for 'newstocks' table
db_config_newstocks = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# Establish connections to MySQL for both tables
conn_stocks = mysql.connector.connect(**db_config_stocks)
conn_newstocks = mysql.connector.connect(**db_config_newstocks)

# Fetching data from the 'stocks' table for Apple, Microsoft, and Tesla
symbols_stocks = ['AAPL', 'MSFT', 'TSLA']
data_stocks = {}

for symbol in symbols_stocks:
    query_stocks = f"SELECT date, open FROM stocks WHERE symbol = '{symbol}'"
    cursor_stocks = conn_stocks.cursor()
    cursor_stocks.execute(query_stocks)
    result_stocks = cursor_stocks.fetchall()
    data_stocks[symbol] = {'date': [], 'open': []}
    for row in result_stocks:
        data_stocks[symbol]['date'].append(row[0])
        data_stocks[symbol]['open'].append(row[1])
    cursor_stocks.close()

# Fetching data from the 'newstocks' table for Google, IBM, and Nvidia
symbols_newstocks = ['GOOGL', 'IBM', 'NVDA']
data_newstocks = {}

for symbol in symbols_newstocks:
    query_newstocks = f"SELECT date, open FROM newstocks WHERE symbol = '{symbol}'"
    cursor_newstocks = conn_newstocks.cursor()
    cursor_newstocks.execute(query_newstocks)
    result_newstocks = cursor_newstocks.fetchall()
    data_newstocks[symbol] = {'date': [], 'open': []}
    for row in result_newstocks:
        data_newstocks[symbol]['date'].append(row[0])
        data_newstocks[symbol]['open'].append(row[1])
    cursor_newstocks.close()

# Close connections to databases
conn_stocks.close()
conn_newstocks.close()

# Plotting the data as a line plot
plt.figure(figsize=(10, 6))

for symbol in data_stocks:
    plt.plot(data_stocks[symbol]['date'], data_stocks[symbol]['open'], label=symbol)

for symbol in data_newstocks:
    plt.plot(data_newstocks[symbol]['date'], data_newstocks[symbol]['open'], label=symbol)

plt.title('Stock Open Prices Comparison')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 2 
import mysql.connector
import matplotlib.pyplot as plt

# MySQL database connection details for 'stocks' table
db_config_stocks = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# MySQL database connection details for 'newstocks' table
db_config_newstocks = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Duke#7539',
    'database': 'Project1'
}

# Establish connections to MySQL for both tables
conn_stocks = mysql.connector.connect(**db_config_stocks)
conn_newstocks = mysql.connector.connect(**db_config_newstocks)

# Fetching data from the 'stocks' table for Apple, Microsoft, and Tesla
symbols_stocks = ['AAPL', 'MSFT', 'TSLA']
data_stocks = {}

for symbol in symbols_stocks:
    query_stocks = f"SELECT date, open FROM stocks WHERE symbol = '{symbol}'"
    cursor_stocks = conn_stocks.cursor()
    cursor_stocks.execute(query_stocks)
    result_stocks = cursor_stocks.fetchall()
    data_stocks[symbol] = {'date': [], 'open': []}
    for row in result_stocks:
        data_stocks[symbol]['date'].append(row[0])
        data_stocks[symbol]['open'].append(row[1])
    cursor_stocks.close()

# Fetching data from the 'newstocks' table for Google, IBM, and Nvidia
symbols_newstocks = ['GOOGL', 'IBM', 'NVDA']
data_newstocks = {}

for symbol in symbols_newstocks:
    query_newstocks = f"SELECT date, open FROM newstocks WHERE symbol = '{symbol}'"
    cursor_newstocks = conn_newstocks.cursor()
    cursor_newstocks.execute(query_newstocks)
    result_newstocks = cursor_newstocks.fetchall()
    data_newstocks[symbol] = {'date': [], 'open': []}
    for row in result_newstocks:
        data_newstocks[symbol]['date'].append(row[0])
        data_newstocks[symbol]['open'].append(row[1])
    cursor_newstocks.close()

# Close connections to databases
conn_stocks.close()
conn_newstocks.close()

# Plotting the data as a line plot
plt.figure(figsize=(10, 6))

for symbol in data_stocks:
    plt.plot(data_stocks[symbol]['date'], data_stocks[symbol]['open'], label=symbol)
    # Find and annotate highest and lowest points for stocks from 'stocks' table
    highest_point_stocks = max(data_stocks[symbol]['open'])
    lowest_point_stocks = min(data_stocks[symbol]['open'])
    date_highest_stocks = data_stocks[symbol]['date'][data_stocks[symbol]['open'].index(highest_point_stocks)]
    date_lowest_stocks = data_stocks[symbol]['date'][data_stocks[symbol]['open'].index(lowest_point_stocks)]
    
    plt.scatter(date_highest_stocks, highest_point_stocks, marker='^', color='green', label='Highest')
    plt.scatter(date_lowest_stocks, lowest_point_stocks, marker='v', color='red', label='Lowest')
    
    plt.text(date_highest_stocks, highest_point_stocks, f'{highest_point_stocks}', ha='right', va='bottom', fontsize=8)
    plt.text(date_lowest_stocks, lowest_point_stocks, f'{lowest_point_stocks}', ha='right', va='bottom', fontsize=8)

for symbol in data_newstocks:
    plt.plot(data_newstocks[symbol]['date'], data_newstocks[symbol]['open'], label=symbol)
    # Find and annotate highest and lowest points for stocks from 'newstocks' table
    highest_point_newstocks = max(data_newstocks[symbol]['open'])
    lowest_point_newstocks = min(data_newstocks[symbol]['open'])
    date_highest_newstocks = data_newstocks[symbol]['date'][data_newstocks[symbol]['open'].index(highest_point_newstocks)]
    date_lowest_newstocks = data_newstocks[symbol]['date'][data_newstocks[symbol]['open'].index(lowest_point_newstocks)]
    
    plt.scatter(date_highest_newstocks, highest_point_newstocks, marker='^', color='blue', label='Highest')
    plt.scatter(date_lowest_newstocks, lowest_point_newstocks, marker='v', color='orange', label='Lowest')
    
    plt.text(date_highest_newstocks, highest_point_newstocks, f'{highest_point_newstocks}', ha='right', va='bottom', fontsize=8)
    plt.text(date_lowest_newstocks, lowest_point_newstocks, f'{lowest_point_newstocks}', ha='right', va='bottom', fontsize=8)

plt.title('Stock Open Prices Comparison')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

