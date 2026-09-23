import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()

if PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")
else:
    raise SystemExit(
        f"Unknown PROVIDER '{PROVIDER}'. Use groq."
    )

if not API_KEY:
    raise SystemExit(
        "No API key found. Check your .env file."
    )

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

EVENT_COSTS = {
    "food": 8000,
    "decoration": 5000,
    "certificates": 3000,
    "prizes": 6000
}

QUESTIONS = [
    "How much does food cost for the college event?",
    "What is the total cost of food and decoration?",
    "Is the total cost of all event items within a budget of Rs. 25000, and how much will remain?",
    "Write a two-line welcome message for the college event.",
]


def banner(system_name):
    print(
        f"\n=== {system_name} | provider: {PROVIDER} | model: {MODEL} ===\n"
    )