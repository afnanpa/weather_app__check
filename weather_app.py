import requests

API_KEY = "284456250c9de77778fb23752d012eca"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

while True:
    city = input("Enter city name (or 'exit' to quit): ")
    if city.lower() == 'exit':
        break

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        print(f"\nWeather in {city.title()}:")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"🌥️ Condition: {weather.title()}")
        print(f"💧 Humidity: {humidity}%\n")
    else:
        print(f"\n❌ Error: {data.get('message')}\n")
