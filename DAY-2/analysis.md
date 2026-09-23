# Day 2 Task – Reasoning and Acting

## 1. Scenario

The chosen scenario is a college event planning problem.

The event has a budget of Rs. 25,000 with the following expenses:

- Food – Rs. 8,000
- Decoration – Rs. 5,000
- Certificates – Rs. 3,000
- Prizes – Rs. 6,000

Total cost = Rs. 22,000  
Remaining budget = Rs. 3,000

## 2. Direct Prompting

Direct prompting asks the model for an answer without explicitly requesting step-by-step reasoning.

In this scenario, it can answer when all required information is provided in the question. It does not use tools.

Its limitation is that it cannot retrieve information from the event-cost tools used by the ReAct agent.

## 3. Chain-of-Thought Prompting

Chain-of-Thought (CoT) asks the model to solve a problem step by step.

For example:

8,000 + 5,000 + 3,000 + 6,000 = 22,000

25,000 - 22,000 = 3,000

CoT is useful for multi-step calculations, but it does not automatically access external tools.

## 4. ReAct Agent

ReAct combines reasoning with actions and observations.

In this scenario, the agent uses `get_event_cost()` to obtain the four event costs and `calculator()` to calculate the total and remaining budget.

The process is:

Question → Thought → Action → Observation → Final Answer

The main advantage is that ReAct can use tools to obtain information and perform calculations. Its limitation is that additional tool calls can take more time.

## 5. Comparison Table

| Basis | Direct Prompting | CoT | ReAct |
|---|---|---|---|
| Reasoning | Simple | Step-by-step | Reasoning + actions |
| Tool usage | No | No | Yes |
| Multi-step problems | Suitable for simple problems | Useful | Useful with tools |
| Transparency | Final answer | Steps shown | Action/Observation trace |
| Speed | Fast | More processing | More tool calls |
| Consistency | Depends on temperature | Can vary | Can vary |

## 6. Self-Consistency Observation

The same question was run five times using CoT with temperature 0.8.

The runs produced:

- 22000
- 22000
- **22000
- 22,000
- **22000

The program reported a majority of **2 out of 5** because the current implementation compares exact strings.

However, all five responses represent the same numerical answer: **Rs. 22,000**.

This shows that answer formatting can affect majority voting. Normalizing answers before voting would improve the result.

## 7. Suitability Analysis

**Direct Prompting:** Suitable when the required information is already available and the problem is simple.

**CoT:** Suitable for multi-step reasoning and calculations.

**ReAct:** Suitable when the problem requires both reasoning and tool interaction.

## 8. Conclusion

Direct prompting provides a quick answer, CoT provides step-by-step reasoning, and ReAct combines reasoning with tool usage.

The experiment shows that the appropriate approach depends on whether the problem requires simple answering, multi-step reasoning, or external tool interaction.