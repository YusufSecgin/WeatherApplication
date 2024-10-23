import requests
import tkinter as tk
from tkinter import messagebox, font
import math

# OpenWeather API details
API_KEY = 'your_openweather_api_key'  # Replace with your actual OpenWeather API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to get weather data
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        temp = weather_data['main']['temp']
        temp = math.ceil(temp)
        weather_desc = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        return f"Temperature: {temp}°C\nCondition: {weather_desc}", icon
    else:
        return "Weather data not found.", None

# Function to display weather in the GUI
def show_weather():
    city = city_entry.get()
    if city:
        weather_info, icon = get_weather(city)
        if icon:
            result_label.config(text=weather_info)
            emoji = ""
            if icon.startswith('01'):    # Clear
                emoji = "☀️"
            elif icon.startswith('02'):  # Few clouds
                emoji = "🌤️"
            elif icon.startswith('03'):  # Scattered clouds
                emoji = "☁️"
            elif icon.startswith('04'):  # Broken clouds
                emoji = "☁️"
            elif icon.startswith('09'):  # Shower rain
                emoji = "🌧️"
            elif icon.startswith('10'):  # Rain
                emoji = "🌧️"
            elif icon.startswith('11'):  # Thunderstorm
                emoji = "⛈️"
            elif icon.startswith('13'):  # Snow
                emoji = "❄️"
            elif icon.startswith('50'):  # Mist
                emoji = "🌫️"
            result_label.config(text=f"{weather_info}\n{emoji}")
        else:
            messagebox.showwarning("Error", "City not found.")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# Setting up the GUI window
root = tk.Tk()
root.title("AeroMetrix - Weather App")
root.geometry("400x300")
root.configure(bg="#88A9C3")

# Set custom font styles
header_font = font.Font(family="Helvetica", size=20, weight="bold")
label_font = font.Font(family="Helvetica", size=12)

# Header label
header_label = tk.Label(root, text="AeroMetrix", font=header_font, bg="#88A9C3", fg="#FFFFFF")
header_label.pack(pady=10)

# GUI Layout
city_label = tk.Label(root, text="Enter city name:", font=label_font, bg="#88A9C3", fg="#FFFFFF")
city_label.pack(pady=5)

city_entry = tk.Entry(root, font=label_font, width=30, bd=2, relief="solid")
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Get Weather", command=show_weather, bg="#091235", fg="black", font=label_font, relief="raised", bd=2)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=label_font, bg="#88A9C3", fg="#FFFFFF")
result_label.pack(pady=10)

# Quit button
quit_button = tk.Button(root, text="Quit", command=root.quit, bg="#14202E", fg="black", font=label_font, relief="raised", bd=2)
quit_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
