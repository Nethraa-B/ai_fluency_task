from config import client, MODEL
from tools import get_course_fee, calculator

question = "I can pay Rs. 30,000. Which two courses can I take together within this budget?"

print("Q:", question)

# Simple workflow cannot handle this type of question
print("Workflow: Sorry, I can only answer questions about course fees.")

# Agent-style reasoning using the available tools
fees = {
    "CS101": get_course_fee("CS101"),
    "AI202": get_course_fee("AI202"),
    "DS303": get_course_fee("DS303")
}

pairs = [
    ("CS101", "AI202"),
    ("CS101", "DS303"),
    ("AI202", "DS303")
]

for c1, c2 in pairs:
    total = calculator(f"{fees[c1]} + {fees[c2]}")
    if total <= 30000:
        print(f"Agent: {c1} + {c2} = Rs. {total:.0f}")