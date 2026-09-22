import sys
from config import client, MODEL

print("Python version:", sys.version.split()[0])
print("Model:", MODEL)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "Reply with exactly: SETUP OK"
        }
    ],
    temperature=0
)

print(response.choices[0].message.content)
