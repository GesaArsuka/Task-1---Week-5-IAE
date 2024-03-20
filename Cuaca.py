import streamlit as st
import requests
from openai import OpenAI

API_key = "60c3d76f4c0efdbf97ac6d7c40e9da7b"

description = ""
temperature = ""
pressure = ""
windspeed = ""
city_name = ""




def searchCity(city_name) :
    global description, temperature, pressure, windspeed
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
    
    weather = requests.get(url)
    weatherData = weather.json()

    description = weatherData['weather'][0]['description']
    icon = weatherData['weather'][0]['icon']
    temperature = int(weatherData['main']['temp'])-273
    pressure = int(weatherData['main']['humidity'])
    windspeed = int(weatherData['wind']['speed'])
    
    return description, temperature, pressure, windspeed



st.title('Weather app')


city_name = st.text_input("Which city do you want to look for?")

if st.button("Search"):
    
    output = searchCity(city_name)


    url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": f"You are a weather person. Tell me about the weather today in {city_name} using only these info of Weather  described in the following without adding temperature numbers : description of {description} , plus a few recommended activities to do in this weather"
            }
        ]
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "d3df6dc15bmsh342cb4697f76e33p1ee0f0jsn045f39f9f64b",
        "X-RapidAPI-Host": "chatgpt-best-price.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    chat_completion = response.json()
    chat_response = chat_completion['choices'][0]['message']['content']

    st.write(f"The weather in {city_name} today is {description}, with a temperature of {temperature} Celcius, an atmospheric pressure of {pressure} hPa, and windspeed of {windspeed} m/s.\n" , chat_response)

