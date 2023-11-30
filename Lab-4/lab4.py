# Question 1 
import requests
import psycopg2
API_KEY = 'c446b12235ca04ae9dd8acc54f8c9107'
city = input("Enter the city name")
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

db_params = {'dbname': 'joelmendonsa', 'user': 'postgres', 'password': 'Duke#7539', 'host': 'localhost', 'port': 5432}

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

create_table_query = """CREATE TABLE IF NOT EXISTS weather_data (city_name VARCHAR(255), country VARCHAR(255), temperature FLOAT, humidity INT, description VARCHAR(255));"""
cursor.execute(create_table_query)
conn.commit()

response = requests.get(url)
if response.status_code == 200:
    weather_data = response.json()
    temperature, humidity, description = weather_data['main']['temp'], weather_data['main']['humidity'], weather_data['weather'][0]['description']
    country, city_name = weather_data['sys']['country'], weather_data['name']
    insert_query = """INSERT INTO weather_data (city_name, country, temperature, humidity, description) VALUES (%s, %s, %s, %s, %s);"""
    cursor.execute(insert_query, (city_name, country, temperature, humidity, description))
    conn.commit()
    print("Data inserted successfully.")
else:
    print(f"Error: {response.status_code} - {response.text}")
    
cursor.close()
conn.close()
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute("SELECT city_name, country, temperature, humidity, description FROM weather_data")
    rows = cursor.fetchall()
    for row in rows:
        print(f"City: {row[0]}, Country: {row[1]}")
        print(f"Temperature: {row[2]} K")
        print(f"Humidity: {row[3]}%")
        print(f"Description: {row[4]}\n")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

#Question 2 
import psycopg2
import requests

conn_params = {
    'host': 'localhost',
    'database': 'joelmendonsa',
    'user': 'postgres',
    'password': 'Duke#7539',
    'port': 5432,
}

conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()

# Create a table to store the data
create_table_query = """
CREATE TABLE IF NOT EXISTS fakestore_data (
    product_id INT,
    quantity INT,
    customer_firstname TEXT,
    customer_lastname TEXT,
    customer_email TEXT,
    customer_address TEXT
);
"""
cursor.execute(create_table_query)
conn.commit()

api_url = 'https://fakestoreapi.com/carts'

try:
    response = requests.get(api_url)
    if response.status_code == 200:
        cart_data = response.json()
        for i, cart in enumerate(cart_data):
            if i >= 10:
                break
            for product in cart['products']:
                product_id = product['productId']
                quantity = product['quantity']
                user_info = requests.get(f'https://fakestoreapi.com/users/{cart["userId"]}').json()
                firstname = user_info.get('name', {}).get('firstname', 'N/A')
                lastname = user_info.get('name', {}).get('lastname', 'N/A')
                email = user_info.get('email', 'N/A')
                address = user_info.get('address', {})
                address_str = f"{address.get('street', 'N/A')}, {address.get('city', 'N/A')}, {address.get('zipcode', 'N/A')}"
                cursor.execute("""
                    INSERT INTO fakestore_data (product_id, quantity, customer_firstname, customer_lastname, customer_email, customer_address)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """, (product_id, quantity, firstname, lastname, email, address_str))
        conn.commit()
        print("Data inserted into the database.")

    else:
        print(f"Error: {response.status_code} - {response.text}")

except Exception as e:
    print(f"An error occurred: {e}")
    
conn.close()
conn_params = {
    'host': 'localhost',
    'database': 'joelmendonsa',
    'user': 'postgres',
    'password': 'Duke#7539',
    'port': 5432,
}
conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()

cursor.execute("SELECT * FROM fakestore_data;")
rows = cursor.fetchall()

for row in rows:
    product_id, quantity, firstname, lastname, email, address = row
    print(f"Product ID: {product_id}, Quantity: {quantity}")
    print(f"Customer Name: {firstname} {lastname}")
    print(f"Customer Email: {email}")
    print(f"Customer Address: {address}\n")

conn.close()

# Question 3 
import requests
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest
import psycopg2

API_KEY = 'c446b12235ca04ae9dd8acc54f8c9107'
CITY = input("Enter the city name: ")
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}'

response = requests.get(URL)
weather_data = response.json()

data = []
for item in weather_data['list']:
    timestamp = item['dt']
    temperature = item['main']['temp']
    data.append({'timestamp': timestamp, 'temperature': temperature})

df = pd.DataFrame(data)

df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

conn = psycopg2.connect(
    host='localhost',
    database='joelmendonsa',
    user='postgres',
    password='Duke#7539',
    port=5432
)
cursor = conn.cursor()

table_name = "new_weather_data"

cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        timestamp TIMESTAMP,
        temperature FLOAT
    );
""")
conn.commit()

for _, row in df.iterrows():
    cursor.execute(f"""
        INSERT INTO {table_name} (timestamp, temperature)
        VALUES (%s, %s);
    """, (row['timestamp'], row['temperature']))
conn.commit()

cursor.close()
conn.close()

conn = psycopg2.connect(
    host='localhost',
    database='joelmendonsa',
    user='postgres',
    password='Duke#7539',
    port=5432)
cursor = conn.cursor()
table_name = "new_weather_data"
cursor.execute(f"SELECT * FROM {table_name};")

for row in cursor.fetchall():
    timestamp, temperature = row
    print(f"Timestamp: {timestamp}, Temperature: {temperature} K")

cursor.close()
conn.close()
