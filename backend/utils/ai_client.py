from openai import OpenAI
from os import getenv

client = OpenAI(api_key=getenv("OPENAI_API_KEY"))

async def get_insights(text: str):
    response = client.chat.completion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "I am a financial advisor AI"},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message["content"]