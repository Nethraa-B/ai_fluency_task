import json
from config import client, MODEL
from tools import get_course_fee, calculator

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the fee of a course. Never guess fees.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "Course code such as CS101, AI202, or DS303"
                    }
                },
                "required": ["course_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

def run_agent(question):
    messages = [
        {
            "role": "system",
            "content": (
                "You answer questions about private course fees. "
                "Never guess a course fee. Always use get_course_fee. "
                "Use calculator for arithmetic. "
                "If no tool is needed, answer directly."
            )
        },
        {"role": "user", "content": question}
    ]

    for step in range(5):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0
        )

        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            return message.content

        for tool_call in message.tool_calls:
            name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print(
                f"step {step + 1}: {name}({arguments})"
            )

            if name == "get_course_fee":
                result = get_course_fee(arguments["course_code"])

            elif name == "calculator":
                result = calculator(arguments["expression"])

            else:
                result = "Unknown tool"

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })

    return "Maximum steps reached."


questions = [
    "What is the fee for AI202?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "Is DS303 more expensive than CS101, and by how much?",
    "Give me a two-line welcome message."
]

for q in questions:
    print("Q:", q)
    print("A:", run_agent(q))
    print()