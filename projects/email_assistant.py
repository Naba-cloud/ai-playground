#Email assistant using OpenAI.
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
openai = OpenAI(
    api_key=os.getenv("OPEN_AI_KEY")
)
def emailAssistant():
    input_text = input("Enter the purpose of the email: ")
    prompt=f"Give me a professional email template for intent: {input_text}"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful email assistant that helps people to get client."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
email = emailAssistant()
print(email)

