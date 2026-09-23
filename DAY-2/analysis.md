\# Day 2 Task – Reasoning and Acting: Direct Prompting, Chain-of-Thought and ReAct



\## 1. Scenario



The chosen scenario is a course-fee calculation problem. A student wants to compare different course costs after scholarships and determine the amount that must be paid.



The scenario contains both reasoning questions and a question requiring external information. The course fees are obtained using a tool, while the scholarship calculations and comparisons require reasoning and calculation.



\## 2. Direct Prompting



Direct prompting asks the model for the answer without explicitly requesting visible step-by-step reasoning. The model responds directly using the information available in the prompt and its existing knowledge.



In this scenario, direct prompting can solve questions where all required numerical information is already provided. It can perform straightforward calculations and return an answer immediately. However, it does not have access to the course-fee tool in this approach, so it cannot reliably obtain a fee that is not provided in the prompt.



Direct prompting does not use tools. The model receives the question, processes it, and produces the final response directly.



Its main limitation in this scenario is the lack of external information access. If the required course fee is missing, the model cannot call the course-fee function to retrieve it.



\## 3. Chain-of-Thought Prompting



Chain-of-Thought prompting asks the model to reason through a problem step by step before giving the final answer.



For example, for a student taking courses costing Rs. 12,000, Rs. 18,000 and Rs. 15,000 with a 15% scholarship and four equal instalments, the model can first calculate the total, calculate the scholarship, find the amount payable, and finally divide it into four instalments.



The correct calculation is:



Total = Rs. 12,000 + Rs. 18,000 + Rs. 15,000 = Rs. 45,000



Scholarship = 15% of Rs. 45,000 = Rs. 6,750



Amount payable = Rs. 45,000 - Rs. 6,750 = Rs. 38,250



Each instalment = Rs. 38,250 / 4 = Rs. 9,562.50



Chain-of-Thought can improve multi-step reasoning because the problem is divided into intermediate steps. However, it still cannot fetch facts that are not available to the model. It does not automatically gain access to the course-fee tool simply because it is asked to reason step by step.



\## 4. ReAct Agent



ReAct combines reasoning with actions and observations. Instead of only producing a final answer, the agent can determine what information it needs, call a tool, observe the result, and continue reasoning.



For the course-fee scenario, the ReAct agent can call `get\_course\_fee()` to obtain the required course fees. It can then use the calculator tool to perform the scholarship calculations.



The cycle is:



Question → Thought → Action → Observation → Thought → Action → Observation → Final Answer.



In the experiment, the ReAct agent retrieved the three course fees and used the calculator for the two scholarship calculations. It then compared the results and produced the final answer.



The main advantage in this scenario is that ReAct can obtain information through tools before completing the reasoning. Its limitation is that it requires correctly implemented tools and additional tool calls, which can make the process longer than a direct response.



\## 5. Comparison Table



| Basis for comparison | Direct prompting | Chain-of-Thought | ReAct agent |

|---|---|---|---|

| Reasoning depth | Low to moderate | Higher for multi-step problems | High, with reasoning between actions |

| Tool usage | No | No tool access in this experiment | Yes |

| Reliability on multi-step questions | Suitable for simple problems | Better for multi-step reasoning | Suitable when reasoning and external information are both required |

| Transparency | Final answer is shown without visible reasoning | Intermediate reasoning steps are requested | Thought, Action and Observation trace shows the process |

| Speed / cost | Fast and usually lowest | More tokens and processing than direct prompting | Additional tool calls can increase time and cost |

| Consistency across repeated runs | Depends on temperature | Can vary at non-zero temperature | Can also vary depending on model and tool decisions |



\## 6. Self-Consistency Observation



The Chain-of-Thought instalment question was run five times at a non-zero temperature.



The five runs all produced the numerical answer Rs. 9,562.50 per instalment, although the wording varied slightly between runs.



The majority answer was Rs. 9,562.50 per instalment, and it was correct.



The same experiment was then run with temperature set to 0. All five runs again produced Rs. 9,562.50 per instalment with essentially identical wording.



This shows that temperature affects variation between repeated model outputs. A non-zero temperature allows more variation, while temperature 0 produced consistent outputs in this experiment.



\## 7. Suitability Analysis



For this particular scenario, ReAct is suitable when the required course-fee information is not already available in the question because it can use a tool to retrieve the missing information and then perform calculations.



Direct prompting is suitable when all required information is already available and the problem is simple enough to answer directly.



Chain-of-Thought is useful when the required information is already available but the problem involves several reasoning steps. It can make the calculation process easier to follow, but it cannot independently retrieve missing information.



Therefore, the choice depends on the problem. The important difference is not simply whether one approach can calculate an answer, but whether the problem requires external information and tool interaction.



\## 8. Conclusion



Direct prompting is appropriate for straightforward questions where the required information is already available and a quick answer is sufficient.



Chain-of-Thought is appropriate for multi-step reasoning problems where the required information is already available. It provides a structured reasoning process before the final answer.



ReAct is appropriate when a problem requires both reasoning and interaction with external tools or information sources. It interleaves Thought, Action and Observation so that the agent can obtain information and use the results before reaching a final answer.



The experiment demonstrates that the three approaches differ mainly in how they reason, whether they can use tools, how transparent their process is, and how much computation or interaction is required.

