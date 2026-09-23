import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

BASE_URL = "https://api.groq.com/openai/v1"
API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)
