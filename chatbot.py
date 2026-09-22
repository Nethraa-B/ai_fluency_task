from config import client, MODEL

questions = [
    "What is the fee for AI202?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "Is DS303 more expensive than CS101, and by how much?",
    "Give me a two-line welcome message."
]

for q in questions:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": q}
        ],
        temperature=0
    )
    print("Q:", q)
    print("A:", response.choices[0].message.content)
    print()
    