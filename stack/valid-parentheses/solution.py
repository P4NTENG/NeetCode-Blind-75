def isValid(s: str) -> bool:
    stack = []
    brackets = {"(": ")", "{": "}", "[": "]"}
    for bracket in s:
        if bracket in "({[":
            stack.append(brackets[bracket])
        else:
            if not stack or bracket != stack.pop():
                return False

    return not stack


print(isValid("({[})"))
