from weather import fetch_weather

city = input("Enter city: ")

data = fetch_weather(city)

temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
weather = data["weather"][0]["description"]
wind = data["wind"]["speed"]

print(f"Temprature: {temp} C")
print(f"Weather: {weather}")
print(f"Humidity: {humidity}%")
print(f"Windspeed: {wind}m/s")