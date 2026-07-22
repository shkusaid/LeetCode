def outer_most_parenthesis(s):
    opened = 0
    result = []
    for ch in s:
        if ch == "(":
            opened += 1
            if opened > 1:
                result.append(ch)
        else:
            opened -= 1
            if opened > 0:
                result.append(ch)
    return "".join(result)

s = "(()())(())"
print(outer_most_parenthesis(s))
