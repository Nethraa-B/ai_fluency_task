def read_course_fee(course_code):
    try:
        with open("fee_data.txt", "r") as file:
            for line in file:
                code, fee = line.strip().split(" = ")
                if code == course_code:
                    return fee
        return f"Course {course_code} was not found."
    except Exception as e:
        return f"Tool error: {e}"
