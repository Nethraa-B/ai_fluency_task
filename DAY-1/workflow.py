import re

COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}

questions = [
    "What is the fee for AI202?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "Is DS303 more expensive than CS101, and by how much?",
    "Give me a two-line welcome message."
]

for q in questions:
    q_upper = q.upper()

    if "AI202" in q_upper and "FEE" in q_upper and "TOTAL" not in q_upper:
        print("Fee for AI202: Rs. 18,000")

    elif "TOTAL" in q_upper and "CS101" in q_upper and "AI202" in q_upper:
        total = (12000 + 18000) * 0.9
        print(f"Total fee: Rs. {total:,.0f}")

    else:
        print("Sorry, I do not have a rule for this type of question.")

    print()