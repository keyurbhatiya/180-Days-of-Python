# Day 43: API Integration Project (Fetching Weather Data)  

import requests

# Function to fetch weather data
def get_weather(city):
    api_key = "2542fd86bb601bb39175e2c2f7d85729"  # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return weather
    else:
        return f"Error: Unable to fetch data, status code {response.status_code}"

# Example usage
city = "Ahmedabad"
weather_data = get_weather(city)
print(weather_data)