import requests

api_key = "YOUR_API_KEY"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    print("\n🌤 Weather Report")
    print("-----------------------")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]["feels_like"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
    print("Wind Speed:", data["wind"]["speed"], "m/s")
else:
    print("Error:", data["message"])
