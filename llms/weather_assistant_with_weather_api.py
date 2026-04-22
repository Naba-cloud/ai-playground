#In this you will learn how to create weather assistant and use external function so AI will give you accurate output
import requests
from openai import OpenAI
import os
import dotenv
dotenv.load_dotenv()
openai = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))
def get_weather(city):
    api_key = os.getenv("OPEN_WEATHER_MAP_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The weather in {city} is currently {weather_description} with a temperature of {temperature}°C."
    else:
        return "Sorry, I couldn't retrieve the weather information at the moment."
def weather_assistant(city):
    weather_info = get_weather(city)
    prompt = f"User: What is the weather like in {city}?\nAssistant: {weather_info}\nUser: Can you give me more details about the weather in {city}?"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "system", "content": "You are a helpful weather assistant that provides detailed weather information based on the user's query."}
        ],
        

    )
    return response.choices[0].message.content
city = input("Enter the city name: ")
print(weather_assistant(city))  