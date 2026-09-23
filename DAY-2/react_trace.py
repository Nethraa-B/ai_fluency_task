from tools import get_event_cost, calculator
from config import banner

QUESTION = (
    "A college is organizing a technical event with a budget of Rs. 25000. "
    "What is the total cost of food, decoration, certificates, and prizes, "
    "and how much money will remain?"
)


def run_react():
    print("QUESTION:", QUESTION)
    print("\n--- the agent's actions and observations ---")

    food = get_event_cost("food")
    print("step 1: get_event_cost({'item': 'food'}) ->", food)

    decoration = get_event_cost("decoration")
    print("step 2: get_event_cost({'item': 'decoration'}) ->", decoration)

    certificates = get_event_cost("certificates")
    print("step 3: get_event_cost({'item': 'certificates'}) ->", certificates)

    prizes = get_event_cost("prizes")
    print("step 4: get_event_cost({'item': 'prizes'}) ->", prizes)

    total = calculator(f"{food}+{decoration}+{certificates}+{prizes}")
    print(
        f"step 5: calculator('{food}+{decoration}+{certificates}+{prizes}') ->",
        total
    )

    remaining = calculator(f"25000-{total}")
    print(
        f"step 6: calculator('25000-{total}') ->",
        remaining
    )

    print(
        f"\nFINAL ANSWER: The total event cost is Rs. {total}. "
        f"The college has Rs. {remaining} remaining from the Rs. 25000 budget."
    )


if __name__ == "__main__":
    banner("REACT: COLLEGE EVENT PLANNER")
    run_react()