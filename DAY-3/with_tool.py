from openai import OpenAI
import os
import json
from dotenv import load_dotenv
from tool import read_course_fee

load_dotenv("../.env")

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

tool_schema = {
    "type": "function",
    "function": {
        "name": "read_course_fee",
        "description": "Look up the fee for a college course code from the local fee file.",
        "parameters": {
            "type": "object",
            "properties": {
                "course_code": {
                    "type": "string",
                    "description": "The course code, such as CS101 or AI202."
                }
            },
            "required": ["course_code"]
        }
    }
}

questions = [
    "What is the fee for CS101?",
    "What is the total fee for CS101 and AI202?",
    "What is an LLM?"
]

for question in questions:
    messages = [{"role": "user", "content": question}]

    print("\nQ:", question)

    for _ in range(3):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=[tool_schema],
            tool_choice="auto",
            temperature=0
        )

        message = response.choices[0].message

        if not message.tool_calls:
            print("TOOL CALL: None")
            print("A:", message.content)
            break

        messages.append(message)

        for call in message.tool_calls:
            print("TOOL CALL:", call.function.name, call.function.arguments)

            args = json.loads(call.function.arguments)
            result = read_course_fee(**args)

            print("TOOL RESULT:", result)

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })
