import requests

city = input("Enter a city: ")
url = "https://geocoding-api.open-meteo.com/v1/search"
params = {"name": city}
response = requests.get(url, params=params)
data = response.json()

latitude = data["results"][0]["latitude"]
longitude = data["results"][0]["longitude"]

weather_url = "https://api.open-meteo.com/v1/forecast"

print(latitude)

print(longitude)

print(data)

print("Weather for", city)

if city == "Houston":
    temperature = 85
    condition = "Sunny"
    print("Temperature:", temperature)
    print("Condition:", condition)

elif city == "Dallas":
    temperature = 82
    condition = "Sunny"
    print("Temperature:", temperature)
    print("Condition:", condition)

elif city == "New York":
    temperature = 72
    condition = "Cloudy"
    print("Temperature:", temperature)
    print("Condition:", condition)
else: 
    print("City not found.")
    







