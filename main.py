import tkinter as tk
from weather import fetch_weather

window = tk.Tk()
window.title("Weather App")
window.geometry("400x300")

city_label = tk.Label(window, text="Enter City")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

temp_label = tk.Label(window, text="Temperature: ")
temp_label.pack()

weather_label = tk.Label(window, text="Weather: ")
weather_label.pack()

humidity_label = tk.Label(window, text="Humidity: ")
humidity_label.pack()

wind_label = tk.Label(window, text="Wind Speed: ")
wind_label.pack()

def get_weather():
    city = city_entry.get()

    data = fetch_weather(city)

    if data is None or data["cod"] != 200:
        temp_label.config(text="City not found")
        return

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind = data["wind"]["speed"]

    temp_label.config(text=f"Temperature: {temp} °C")
    weather_label.config(text=f"Weather: {weather}")
    humidity_label.config(text=f"Humidity: {humidity}%")
    wind_label.config(text=f"Wind Speed: {wind} m/s")

search_button = tk.Button(window, text="Search", command=get_weather)
search_button.pack()

window.mainloop()