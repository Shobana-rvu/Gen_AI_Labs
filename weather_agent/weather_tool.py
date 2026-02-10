import requests
import os

OPENWEATHER_API_KEY = st.secrets["OPENWEATHER_API_KEY"]

def get_weather(city: str):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != "200":
        return "Weather data not available."

    forecasts = data["list"][:8]  # ~2 days (3-hour intervals)
    summary = []

    for item in forecasts:
        temp = item["main"]["temp"]
        desc = item["weather"][0]["description"]
        summary.append(f"{temp}°C, {desc}")

    return ", ".join(summary)
