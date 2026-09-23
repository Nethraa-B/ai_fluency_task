import ast
import operator
from config import EVENT_COSTS


def get_event_cost(item: str) -> str:
    """Look up the cost of an event item."""
    cost = EVENT_COSTS.get(item.strip().lower())

    if cost is not None:
        return str(cost)

    return f"Unknown event item: {item}"


_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg
}


def _evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.left),
            _evaluate(node.right)
        )

    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.operand)
        )

    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression."""
    try:
        return str(
            _evaluate(
                ast.parse(expression, mode="eval").body
            )
        )
    except Exception as error:
        return f"Calculator error: {error}"


TOOL_FUNCTIONS = {
    "get_event_cost": get_event_cost,
    "calculator": calculator
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_event_cost",
            "description": "Get the cost in rupees for an item needed for a college event.",
            "parameters": {
                "type": "object",
                "properties": {
                    "item": {
                        "type": "string"
                    }
                },
                "required": ["item"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Evaluate an arithmetic expression using + - * / and brackets.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


if __name__ == "__main__":
    print("get_event_cost('food') ->", get_event_cost("food"))
    print(
        "calculator('8000 + 5000 + 3000 + 6000') ->",
        calculator("8000 + 5000 + 3000 + 6000")
    )
    print(
        "calculator('25000 - 22000') ->",
        calculator("25000 - 22000")
    )