COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}

def get_course_fee(course_code):
    return COURSE_FEES.get(course_code.upper())

def calculator(expression):
    allowed = set("0123456789+-*/(). ")
    if not all(c in allowed for c in expression):
        raise ValueError("Invalid expression")
    return eval(expression, {"__builtins__": {}}, {})


if __name__ == "__main__":
    print("get_course_fee('ai202') ->", get_course_fee("ai202"))
    print("calculator('(12000 + 18000) * 0.9') ->",
          calculator("(12000 + 18000) * 0.9"))
    print("calculator('15000 - 12000') ->",
          calculator("15000 - 12000"))