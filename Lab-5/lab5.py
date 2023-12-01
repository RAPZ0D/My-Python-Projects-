# Question 1
import requests

def get_fakestore_users():
    url = "https://fakestoreapi.com/users"
    response = requests.get(url)
    users = []

    if response.status_code == 200:
        users = response.json()
    else:
        print("Failed to retrieve user data")

    return users

def get_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return (
            weather_data['main']['temp'],
            weather_data['main']['humidity'],
            weather_data['wind']['speed']
        )
    else:
        print(f"Failed to retrieve weather data for {city}")
        return None, None, None

# Main execution
api_key = "c446b12235ca04ae9dd8acc54f8c9107"

users = get_fakestore_users()

if users:
    cities = ["New York", "London", "Paris", "Tokyo", "Sydney"]
    humidity_list = []
    temperature_list = []
    wind_speed_list = []

    for i, user in enumerate(users[:5]):
        print(f"Name: {user['name']['firstname']} {user['name']['lastname']}")
        city = cities[i] if i < len(cities) else "Unknown"
        print(f"User's first city: {city}")

        temperature, humidity, wind_speed = get_weather_data(api_key, city)

        # Append weather data to respective lists
        temperature_list.append(temperature)
        humidity_list.append(humidity)
        wind_speed_list.append(wind_speed)

    print("Temperature List:", temperature_list)
    print("Humidity List:", humidity_list)
    print("Wind Speed List:", wind_speed_list)

from sklearn.linear_model import LinearRegression

features = list(zip(temperature_list, humidity_list, wind_speed_list))
target = [25, 20, 15, 30, 22]
model = LinearRegression()
model.fit(features, target)
new_city = "Berlin"
new_temperature, new_humidity, new_wind_speed = get_weather_data(api_key, new_city)
predicted_temperature = model.predict([[new_temperature, new_humidity, new_wind_speed]])
print(f"Predicted temperature for {new_city}: {predicted_temperature[0]}")

import psycopg2
conn = psycopg2.connect(
    host='localhost',
    database='joelmendonsa',
    user='postgres',
    password='Duke#7539',
    port=5432
)
cursor = conn.cursor()
create_table_query = '''CREATE TABLE IF NOT EXISTS predictions (
                            city TEXT,
                            predicted_value FLOAT
                        )'''
cursor.execute(create_table_query)
conn.commit()
insert_query = '''INSERT INTO predictions (city, predicted_value) VALUES (%s, %s)'''
cursor.execute(insert_query, (new_city, predicted_temperature[0]))
conn.commit()

cursor.close()
conn.close()

conn = psycopg2.connect(
    host='localhost',
    database='joelmendonsa',
    user='postgres',
    password='Duke#7539',
    port=5432
)

cursor = conn.cursor()

select_query = "SELECT city, predicted_value FROM predictions"
cursor.execute(select_query)

rows = cursor.fetchall()

if rows:
    print("City\t\tPredicted Value")
    print("------------------------------")
    for row in rows:
        city, predicted_value = row
        print(f"{city}\t\t{predicted_value}")
else:
    print("No data found.")

cursor.close()
conn.close()

# Question 2 

import requests
import random

def get_fakestore_users():
    url = "https://fakestoreapi.com/users"
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()
        return users
    else:
        print("Failed to retrieve user data")
        return None

def get_fakestore_products():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)

    if response.status_code == 200:
        products = response.json()
        return products
    else:
        print("Failed to retrieve product data")
        return None

def get_random_item(items):
    return random.choice(items)
users = get_fakestore_users()
products = get_fakestore_products()

if users and products:
    selected_user = get_random_item(users)
    selected_product = get_random_item(products)
    response = random.choice(['Yes', 'No'])
    print("User Profile:")
    print(f"Name: {selected_user['name']['firstname']} {selected_user['name']['lastname']}")
    print(f"Email: {selected_user['email']}")
    print("Address: {} {}".format(selected_user['address']['street'], selected_user['address']['city']))
    print("-----------------------")

    print("Product:")
    print(f"Title: {selected_product['title']}")
    print(f"Category: {selected_product['category']}")
    print(f"Price: ${selected_product['price']}")
    print(f"User Response: {response}")
else:
    print("No user profiles or product details found.")

import requests
import random
import psycopg2

def get_fakestore_users():
    url = "https://fakestoreapi.com/users"
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()
        return users
    else:
        print("Failed to retrieve user data")
        return None

def get_fakestore_products():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)

    if response.status_code == 200:
        products = response.json()
        return products
    else:
        print("Failed to retrieve product data")
        return None

def get_random_item(items):
    return random.choice(items)

# PostgreSQL connection
conn = psycopg2.connect(
    host='localhost',
    database='joelmendonsa',
    user='postgres',
    password='Duke#7539',
    port=5432
)
cursor = conn.cursor()

# Create the table if it doesn't exist
create_table_query = '''
    CREATE TABLE IF NOT EXISTS product_recommendation (
        user_firstname TEXT,
        user_lastname TEXT,
        user_email TEXT,
        user_address TEXT,
        product_title TEXT,
        product_category TEXT,
        product_price FLOAT,
        user_response TEXT
    )
'''
cursor.execute(create_table_query)
conn.commit()

users = get_fakestore_users()
products = get_fakestore_products()

if users and products:
    selected_user = get_random_item(users)
    selected_product = get_random_item(products)
    user_response = random.choice(['Yes', 'No'])

    insert_query = '''
        INSERT INTO product_recommendation (user_firstname, user_lastname, user_email, user_address, product_title, product_category, product_price, user_response)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_query, (
        selected_user['name']['firstname'],
        selected_user['name']['lastname'],
        selected_user['email'],
        f"{selected_user['address']['street']} {selected_user['address']['city']}",
        selected_product['title'],
        selected_product['category'],
        selected_product['price'],
        user_response
    ))
    conn.commit()

    print("Data stored successfully in the product_recommendation table.")
else:
    print("No user profiles or product details found.")

cursor.close()
conn.close()

conn = psycopg2.connect(
    host='localhost',
    database='joelmendonsa',
    user='postgres',
    password='Duke#7539',
    port=5432
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM product_recommendation")
rows = cursor.fetchall()

if rows:
    for row in rows:
        print("User Profile:")
        print(f"Name: {row[0]} {row[1]}")
        print(f"Email: {row[2]}")
        print(f"Address: {row[3]}")
        print("-----------------------")
        print("Product:")
        print(f"Title: {row[4]}")
        print(f"Category: {row[5]}")
        print(f"Price: ${row[6]}")
        print(f"User Response: {row[7]}")
        print("=======================")
else:
    print("No product recommendations found.")

cursor.close()
conn.close()

# Question 3
import requests
import psycopg2

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Failed to retrieve weather data.")
        return None

def get_fakestore_users():
    url = "https://fakestoreapi.com/users"
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()
        return users
    else:
        print("Failed to retrieve user data")
        return None

api_key = "c446b12235ca04ae9dd8acc54f8c9107"  # OpenWeatherMap API key

conn = psycopg2.connect(
    host='localhost',
    database='joelmendonsa',
    user='postgres',
    password='Duke#7539',
    port=5432
)

cursor = conn.cursor()

create_table_query = '''
    CREATE TABLE IF NOT EXISTS user_recommendations (
        user_firstname TEXT,
        user_lastname TEXT,
        user_email TEXT,
        city TEXT,
        temperature FLOAT,
        humidity FLOAT,
        weather_condition TEXT,
        latitude FLOAT,
        longitude FLOAT,
        recommended_product TEXT
    )
'''
cursor.execute(create_table_query)
conn.commit()

users = get_fakestore_users()

if users:
    for user in users:
        city_name = user['address']['city']
        weather_info = get_weather(api_key, city_name)

        if weather_info:
            weather_condition = weather_info['weather'][0]['main'].lower()
            recommended_product = None

            if "sunny" in weather_condition:
                recommended_product = "Sunglasses"
            elif "cloud" in weather_condition:
                recommended_product = "Jacket"
            elif "rain" in weather_condition:
                recommended_product = "Boots"
            elif "snow" in weather_condition or weather_info['main']['temp'] < 0:
                recommended_product = "Coat"

            cursor.execute('''
                INSERT INTO user_recommendations (user_firstname, user_lastname, user_email, city, temperature, humidity, weather_condition, latitude, longitude, recommended_product)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                user['name']['firstname'],
                user['name']['lastname'],
                user['email'],
                city_name,
                weather_info['main']['temp'],
                weather_info['main']['humidity'],
                weather_condition,
                weather_info['coord']['lat'],
                weather_info['coord']['lon'],
                recommended_product
            ))
            conn.commit()

    print("Data stored successfully in user_recommendations table.")
else:
    print("No user profiles found.")

cursor.close()
conn.close()

def get_weather(api_key, lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Failed to retrieve weather data.")
        return None

def get_recommendation(weather_condition, temperature):
    if "sunny" in weather_condition:
        return "Sunglasses"
    elif "cloud" in weather_condition:
        return "Jacket"
    elif "rain" in weather_condition:
        return "Boots"
    elif "snow" in weather_condition or temperature < 0:
        return "Coat"
    else:
        return "No specific recommendation based on weather."

api_key = "c446b12235ca04ae9dd8acc54f8c9107"  # OpenWeatherMap API key
latitude = 29.4241
longitude = -98.4936

weather_info = get_weather(api_key, latitude, longitude)

if weather_info:
    print("Weather Details:")
    print("Temperature:", weather_info['main']['temp'])
    print("Humidity:", weather_info['main']['humidity'])
    print("Weather Condition:", weather_info['weather'][0]['main'])
    print("Description:", weather_info['weather'][0]['description'])
    
    recommended_product = get_recommendation(weather_info['weather'][0]['main'].lower(), weather_info['main']['temp'])
    print("Recommended Product:", recommended_product)
else:
    print("No weather data found for the specified location.")

# Question 4
import psycopg2
import requests

# Function to initialize the PostgreSQL table
def initialize_table():
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='joelmendonsa',
            user='postgres',
            password='Duke#7539',
            port=5432
        )

        cursor = connection.cursor()

        # Create inventory table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id SERIAL PRIMARY KEY,
                category TEXT,
                price REAL,
                category_count INTEGER DEFAULT 0
            );
        ''')

        connection.commit()
        connection.close()

    except psycopg2.Error as e:
        print(f"Error initializing table: {e}")

# Function to update the inventory table and category_count column
def update_inventory():
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='joelmendonsa',
            user='postgres',
            password='Duke#7539',
            port=5432
        )

        cursor = connection.cursor()

        endpoint = 'https://fakestoreapi.com/products'

        response = requests.get(endpoint)
        if response.status_code == 200:
            products = response.json()

            for product in products:
                category = product['category']
                price = product['price']

                cursor.execute('SELECT COUNT(*) FROM inventory WHERE category = %s', (category,))
                category_count = cursor.fetchone()[0]

                if category_count == 0:
                    # Category is being added
                    cursor.execute('INSERT INTO inventory (category, price, category_count) VALUES (%s, %s, 1)', (category, price))
                else:
                    # Category is already in inventory
                    cursor.execute('UPDATE inventory SET category_count = category_count + 1 WHERE category = %s', (category,))

            connection.commit()
        else:
            print(f"Failed to fetch products. Status code: {response.status_code}")

        connection.close()

    except psycopg2.Error as e:
        print(f"Error updating inventory: {e}")

if __name__ == "__main__":
    initialize_table()
    update_inventory()

def sell_category():
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='joelmendonsa',
            user='postgres',
            password='Duke#7539',
            port=5432
        )

        cursor = connection.cursor()

        category_name = input("Enter the category name: ")
        quantity_sold = int(input("Enter the quantity sold: "))

        # Check if the category exists and has enough count
        cursor.execute('SELECT category_count FROM inventory WHERE category = %s', (category_name,))
        category_count = cursor.fetchone()

        if category_count is not None and category_count[0] >= quantity_sold:
            updated_count = category_count[0] - quantity_sold
            cursor.execute('UPDATE inventory SET category_count = %s WHERE category = %s', (updated_count, category_name))
            connection.commit()
            print(f"Sold {quantity_sold} of {category_name}. Updated count: {updated_count}")
        else:
            print(f"Not enough quantity available for {category_name}")

        connection.close()

    except psycopg2.Error as e:
        print(f"Error selling category: {e}")

if __name__ == "__main__":
    sell_category()

def restock_categories():
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='joelmendonsa',
            user='postgres',
            password='Duke#7539',
            port=5432
        )

        cursor = connection.cursor()

        # Set the restock threshold and quantity to restock
        restock_threshold = 2
        restock_quantity = 5

        # Retrieve categories with counts below the restock threshold
        cursor.execute('SELECT category, category_count FROM inventory WHERE category_count < %s', (restock_threshold,))
        categories_to_restock = cursor.fetchall()

        if categories_to_restock:
            for category, count in categories_to_restock:
                # Restock the category
                new_count = count + restock_quantity
                cursor.execute('UPDATE inventory SET category_count = %s WHERE category = %s', (new_count, category))
                print(f"Restocked {restock_quantity} items for {category}. New count: {new_count}")

            connection.commit()
        else:
            print("No categories need restocking.")

        connection.close()

    except psycopg2.Error as e:
        print(f"Error restocking categories: {e}")

if __name__ == "__main__":
    restock_categories()

def print_inventory_table():
    try:
        with psycopg2.connect(
            host='localhost',
            database='joelmendonsa',
            user='postgres',
            password='Duke#7539',
            port=5432
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM inventory')
                [print(row) for row in cursor.fetchall()]

    except psycopg2.Error as e:
        print(f"Error printing inventory table: {e}")

if __name__ == "__main__":
    print_inventory_table()
