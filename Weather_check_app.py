import argparse
import requests
import time


API_KEY = 'bd2cca740a4f460e9ed63444230409'


FAVORITE_CITIES_FILE = 'favorite_cities.txt'
REFRESH_INTERVAL = 20  

def load_favorite_cities():
    try:
        with open(FAVORITE_CITIES_FILE, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_favorite_cities(favorite_cities):
    with open(FAVORITE_CITIES_FILE, 'w') as file:
        for city in favorite_cities:
            file.write(city + '\n')
            

def add_favorite_city(city, favorite_cities):
    if city not in favorite_cities:
        favorite_cities.append(city)
        save_favorite_cities(favorite_cities)
        print(f"{city} added to favorites.")
    else:
        print(f"{city} is already in your favorites.")

def remove_favorite_city(city, favorite_cities):
    if city in favorite_cities:
        favorite_cities.remove(city)
        save_favorite_cities(favorite_cities)
        print(f"{city} removed from favorites.")
    else:
        print(f"{city} is not in your favorites.")

def update_favorite_city(old_city, new_city, favorite_cities):
    if old_city in favorite_cities:
        favorite_cities.remove(old_city)
        favorite_cities.append(new_city)
        save_favorite_cities(favorite_cities)
        print(f"{old_city} update with {new_city} in favorites.")
    else:
        print(f"{old_city} is not in your favorites.")  
         

def fetch_weather_data(city_name):
    try:
        base_url = 'http://api.weatherapi.com/v1/current.json'
        params = {
            'q': city_name,
            'key': API_KEY,
     }

        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        return response.json()

    
    except :
        print(f"MESSAGE:Enter the VALID CITY_NAME")
        return None

def print_weather_info(data, city_name):
    if data is not None:
        try:
            weather_description = data['current']['condition']['text']
            temperature = data['current']['temp_c']
            humidity = data['current']['humidity']
            wind_speed = data['current']['wind_kph']

            print(f"Weather in {city_name}:")
            print(f"Description: {weather_description.capitalize()}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} km/h")
        except KeyError:
            print("Invalid response from the weather API. Check the city name and try again.")

def main():
    parser = argparse.ArgumentParser(description='Weather Checking Application')
    parser.add_argument('city', type=str, nargs='?', help='Name of the city ')
    parser.add_argument('-add', type=str, help='Add a city to your favorites')
    parser.add_argument('-remove', type=str, help='Remove a city from your favorites')
    parser.add_argument('-update', nargs=2, metavar=('OLD_CITY', 'NEW_CITY'),
                        help='update a city in your favorites with a new city')
    
    
    args = parser.parse_args()
    
    favorite_cities = load_favorite_cities()
    
    if args.add:
        add_favorite_city(args.add, favorite_cities)
        return
    elif args.remove:
        remove_favorite_city(args.remove, favorite_cities)
        return
    elif args.update:
        old_city, new_city = args.update
        update_favorite_city(old_city, new_city, favorite_cities)
        return
   
    while True:
        if args.city:
            city_name = args.city
        elif favorite_cities:
            city_name = favorite_cities[0]
        else:
            city_name = input("Enter the city name: ")

        weather_data = fetch_weather_data(city_name )

        if weather_data:
            print_weather_info(weather_data, city_name)


        time.sleep(REFRESH_INTERVAL)

print(main())
