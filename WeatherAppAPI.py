import requests
import json
import tkinter as tk

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # Use metric units (Celsius)
            }
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data

        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                print(f"Error: City '{city}' not found.")
            elif response.status_code == 401:
                print("Error: Invalid API key.")
            else:
                print(f"HTTP Error: {e}")
            return None

        except requests.exceptions.ConnectionError:
            print("Error: Unable to connect to the weather service.")
            return None

        except requests.exceptions.Timeout:
            print("Error: Request timed out.")
            return None

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

        except json.JSONDecodeError:
            print("Error: Unable to parse weather data.")
            return None

def main():
    API_KEY = "c158854a90f6d34fcfa3ebc914854b10"
    weather_app = WeatherApp(API_KEY)

    print("Welcome to the Weather App!")
    print("Type 'quit' to exit\n")

    while True:
        city = input("Enter city name: ").strip()

        if city.lower() == 'quit':
            print("Thank you for using Weather App!")
            break

        if not city:
            print("Please enter a valid city name.")
            continue

        weather_data = weather_app.get_weather(city)
        weather_app.display_weather(weather_data)

root = tk.Tk()
root.title("Weather App")
root.geometry("350x250")

title_label = tk.Label(root, text="Weather App", font=("Arial",16))
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial",12), width=25)
city_entry.pack(pady=5)
city_entry.insert(0,"Agra")

result_label = tk.Label(root, text="", font=("Arial",12), justify="left")
result_label.pack(pady=10)

API_KEY = "c158854a90f6d34fcfa3ebc914854b10"
weather_app = WeatherApp(API_KEY)

root = tk.Tk()
root.title("Weather App")
root.geometry("350x250")

title_label = tk.Label(root, text="Weather App", font=("Arial",16))
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial",12), width=25)
city_entry.pack(pady=5)
city_entry.insert(0, "Agra")

result_label = tk.Label(root, text="", font=("Arial",12), justify="left")
result_label.pack(pady=10)

def gui_get_weather():
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    data = weather_app.get_weather(city)

    if "error" in data:
        result_label.config(text=data["error"])
        return

    try:
        city_name = data['name']
        description = data['weather'][0]['description'].capitalize()
        temp = round(data['main']['temp'])
        feels_like = round(data['main']['feels_like'])
        humidity = data['main']['humidity']

        output = (
            f"Weather in {city_name}: {description}\n"
            f"Current Temperature: {temp}°C\n"
            f"Feels Like: {feels_like}°C\n"
            f"Humidity: {humidity}%"
        )

        result_label.config(text=output)

    except KeyError:
        result_label.config(text="Unexpected data format.")

get_button = tk.Button(root, text="Get Weather", font=("Arial",12), command=gui_get_weather)
get_button.pack(pady=10)

root.mainloop()