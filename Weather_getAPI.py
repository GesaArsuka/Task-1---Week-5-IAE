import requests

API_key = "60c3d76f4c0efdbf97ac6d7c40e9da7b"
city_name = "Bandung"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"


weather = requests.get(url)
weather.json()

weatherData = weather.json()

weatherData['weather'][0]['description']
