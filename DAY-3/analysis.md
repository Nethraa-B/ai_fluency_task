# Agentic AI: From Prompt to Action

## 1. Scenario

The scenario used is a college course fee lookup system. A local file contains:

- CS101 = Rs. 13,750
- AI202 = Rs. 22,400
- DS303 = Rs. 16,850

The purpose is to compare a plain LLM with an LLM that has access to one external tool, `read_course_fee`.

## 2. What is an LLM?

A Large Language Model (LLM) is an AI model trained on large amounts of text. It can answer questions, explain concepts, summarize information, and generate text and code.

However, an LLM does not automatically have access to private or local information. When required information is unavailable, it may produce a plausible but incorrect answer.

In this experiment, the plain LLM gave an incorrect course fee because the actual fee was stored in a local file that was not provided to it.

## 3. What is an Agent?

An AI agent goes beyond simply generating a response. It can determine that an external action or tool is needed, call that tool, receive the result, and use the result to produce its final response.

In this scenario, the agent recognized that course-fee information should be obtained using the `read_course_fee` tool.

## 4. What is a Tool and Tool Call?

A tool is an external function that allows an LLM to access information or perform an operation that is not available from the model's own knowledge.

The tool used here is:

`read_course_fee(course_code)`

The tool schema provides:

- **Name:** `read_course_fee`
- **Description:** explains what the tool does and when it should be used
- **Parameters:** specifies the required `course_code` input

The description is important because it helps the model understand the purpose of the tool and decide when it is relevant.

## 5. Step-by-Step Tool Call Flow

1. The user asks a question.
2. The LLM receives the question and available tool schema.
3. The LLM determines whether the tool is required.
4. For a course-fee question, it calls `read_course_fee`.
5. The tool receives the course code.
6. The tool reads the local `fee_data.txt` file.
7. The tool returns the fee as plain text.
8. The LLM uses the returned value to produce the final answer.
9. For a general question such as "What is an LLM?", the model does not call the tool.

## 6. Why Return Plain Text on Failure?

The tool should return an error message as plain text instead of raising an exception.

For example:

`Course XYZ999 was not found.`

This allows the agent to receive the failure as information and continue or explain the problem instead of the entire program crashing.

## 7. Plain LLM vs LLM with One Tool

| Basis | Plain LLM Prompt | LLM with One Tool |
|---|---|---|
| Source of answer | Model's own knowledge | Model knowledge plus tool result |
| Fetch/compute outside own memory | No | Yes, through the tool |
| Reliability for local numeric data | Can be incorrect or guessed | Uses the actual stored value |
| Transparency | Final answer only | Tool call and tool result can be observed |
| Speed/cost | Simpler and generally lower overhead | Additional tool-call overhead |

## 8. Observations

### Question 1: What is the fee for CS101?

**Plain LLM:** Incorrect. It answered $500, while the actual local value is Rs. 13,750.

**Tool-enabled LLM:** Correctly called:

`read_course_fee({"course_code":"CS101"})`

The tool returned Rs. 13,750 and the model used that value in its final answer.

### Question 2: What is the total fee for CS101 and AI202?

**Plain LLM:** It did not provide the total and asked for the individual fees.

**Tool-enabled LLM:** Correctly called the tool for both course codes.

- CS101 = Rs. 13,750
- AI202 = Rs. 22,400
- Total = Rs. 36,150

### Question 3: What is an LLM?

**Plain LLM:** Provided a reasonable explanation without needing an external tool.

**Tool-enabled LLM:** Correctly recognized that the tool was unnecessary and did not call it.

## 9. When Was the Plain LLM Enough?

The plain LLM was sufficient for the general conceptual question about what an LLM is.

For information stored in the local course-fee file, the plain LLM was not reliable because it did not have access to that external information.

## 10. When Was the Tool Necessary?

The tool was necessary for the course-fee questions because the exact values were stored outside the model.

The experiment demonstrates that providing an external tool can improve factual and numeric reliability when the required information is available through that tool.

## 11. Conclusion

A plain LLM is useful when the required information can reasonably be answered from its existing knowledge. However, when a question requires external, local, or exact information, relying only on the model can produce incorrect or incomplete answers.

Adding a single well-defined tool allows the model to obtain the required information and use it in its final response. The experiment demonstrates the difference between simply prompting an LLM and allowing an LLM to take an external action through a tool.
