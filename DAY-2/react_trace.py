"""Day 2, Part D: print the agent's real ReAct trace to compare with your paper trace."""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Day_1')))

from agent import agent

QUESTION = (
    "A college is organizing a technical event with a budget of Rs. 25000. "
    "What is the total cost of food, decoration, certificates, and prizes, "
    "and how much money will remain?"
)

print("QUESTION:", QUESTION, "\n")
print("--- the agent's actions and observations ---")
answer = agent(QUESTION, max_steps=8)
print("\nFINAL ANSWER:", answer)