# 1 OPENWEATHER SUNRISE AND SUNSET 
import requests
from datetime import datetime
api_key = '6d74e9353e3ab512e6405030fd4f8f75'
api_url = 'https://api.openweathermap.org/data/2.5/weather'
city = input("Enter the city name: ")
params = {'q': city,'appid': api_key,'units': 'metric',}
response = requests.get(api_url, params=params)
if response.status_code == 200:
    data = response.json()
    sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
    sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
    print(f"The Sunrise time of {city} is : {sunrise}\nThe Sunset Time of {city} is: {sunset}")
else:
    print(f"Request failed with status code: {response.status_code}")

# Weather comparison tool Step 1 
api_key = '6d74e9353e3ab512e6405030fd4f8f75'
api_url = 'https://api.openweathermap.org/data/2.5/weather'
city1 = input("Enter the first city name: ")
city2 = input("Enter the second city name: ")
def fetch_weather(city_name):
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
    }
    response = requests.get(api_url, params=params)
    return response
response1 = fetch_weather(city1)
response2 = fetch_weather(city2)
def display_weather(response):
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        condition = data['weather'][0]['description']

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Condition: {condition}")
    else:
        print(f"Request failed with status code: {response.status_code}")
print(f"Weather data for {city1}:")
display_weather(response1)
print(f"Weather data for {city2}:")
display_weather(response2)

# Weather tool Step 2 
api_key = '6d74e9353e3ab512e6405030fd4f8f75'
weather_api_url = 'https://api.openweathermap.org/data/2.5/weather'
fake_store_api_url = 'https://fakestoreapi.com/products'
city1 = input("Enter the first city name: ")
city2 = input("Enter the second city name: ")
def fetch_weather(city_name):
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
    }
    response = requests.get(weather_api_url, params=params)
    return response

def display_weather(response):
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        condition = data['weather'][0]['description']
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Condition: {condition}")
        recommended_product = get_recommended_product(condition)
        print(f"Recommended Product: {recommended_product}")
    else:
        print(f"Request failed with status code: {response.status_code}")

print(f"Weather data for {city1}:")
response1 = fetch_weather(city1)
display_weather(response1)
print(f"Weather data for {city2}:")
response2 = fetch_weather(city2)
display_weather(response2)

def get_recommended_product(weather_condition):
    weather_conditions = {
        'clear sky': 'Sunglasses',
        'few clouds': 'Hat',
        'scattered clouds': 'Umbrella',
        'broken clouds': 'Jacket',
        'shower rain': 'Raincoat',
        'rain': 'Umbrella',
        'thunderstorm': 'Umbrella',
        'snow': 'Snow boots',
        'mist': 'Umbrella',
    }
    recommended_product = weather_conditions.get(weather_condition.lower(), 'No recommendation available')
    return recommended_product

