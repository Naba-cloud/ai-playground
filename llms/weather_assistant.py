#i want to built a weather assistant using python and openai API
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPEN_AI_KEY")
openai = OpenAI(
    api_key=api_key)
def get_weather(location):
    prompt = f"What is the weather like in {location}?"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful weather assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
location = input("Enter a location to get the weather: ")
weather = get_weather(location)
print(f"The weather in {location} is: {weather}")   