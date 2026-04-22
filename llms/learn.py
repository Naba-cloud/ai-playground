
from openai import OpenAI
openai = OpenAI(
    api_key=""
)
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Explain AI agents in bullet points with examples."}
    ],
    temperature=0.5,
)
print(response.choices[0].message.content)