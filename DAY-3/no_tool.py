from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv("../.env")

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

questions = [
    "What is the fee for CS101?",
    "What is the total fee for CS101 and AI202?",
    "What is an LLM?"
]

for question in questions:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": question}],
        temperature=0
    )

    print("\nQ:", question)
    print("A:", response.choices[0].message.content)
