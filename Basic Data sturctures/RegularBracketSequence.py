def matching(ch):
    if ch == "(":
        return ")"
    if ch == ")":
        return "("
    if ch == "[":
        return "]"
    if ch == "]":
        return "["
    if ch == "{":
        return "}"
    if ch == "}":
        return "{"


def isLeft(ch):
    return ch in "([{"


def check(s):
    if not s:
        return True

    stack = []
    for ch in s:
        if isLeft(ch):
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack.pop() != matching(ch):
                return False

    return not stack


if check(input()):
    print("yes")
else:
    print("no")

# print(check("[()]"))
# print(check("[(){}[]]"))
# print(check("{((())"))

