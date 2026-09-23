"""Day 2, Part B: Direct Prompting vs Chain-of-Thought."""

from config import client, MODEL, banner


QUESTIONS = [
    "A college is organizing a technical event. "
    "Food costs Rs. 8,000, decoration costs Rs. 5,000, "
    "certificates cost Rs. 3,000, and prizes cost Rs. 6,000. "
    "What is the total cost?",

    "A college event has a budget of Rs. 25,000. "
    "The total cost of food, decoration, certificates, and prizes is Rs. 22,000. "
    "How much money will remain?",

    "A college event has four expenses: food Rs. 8,000, decoration Rs. 5,000, "
    "certificates Rs. 3,000, and prizes Rs. 6,000. "
    "Is the total cost within a budget of Rs. 25,000? "
    "If yes, how much remains?",
]


DIRECT_PROMPT = (
    "You are a helpful assistant. Give only the final answer. "
    "Do not explain."
)

COT_PROMPT = (
    "You are a helpful assistant. Solve the problem step by step. "
    "Number each step and show the calculation in that step. "
    "After the steps, write the last line exactly as: "
    "Final Answer: <answer>"
)


def ask(system_prompt, question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0,
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    banner("CHAIN-OF-THOUGHT COMPARISON")

    for number, question in enumerate(QUESTIONS, start=1):
        print("=" * 72)
        print(f"QUESTION {number}: {question}\n")

        print("--- WITHOUT CoT ---")
        print(ask(DIRECT_PROMPT, question), "\n")

        print("--- WITH CoT ---")
        print(ask(COT_PROMPT, question), "\n")