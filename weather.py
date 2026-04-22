import requests

API_KEY = "6bbf47443d9949f7d14c0e35ea1c1580"

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        return None

    condition = data["weather"][0]["main"].lower()

    # Default
    icon = ""
    background = ""

    if "clear" in condition:
        icon = "☀"
        background = "sunny"
    elif "rain" in condition:
        icon = "🌧"
        background = "rain"
    elif "cloud" in condition:
        icon = "☁"
        background = "cloud"
    else:
        icon = "🌙"
        background = "night"

    weather = {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "icon": icon,
        "background": background
    }

    return weather
