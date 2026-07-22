def minimum_length(s):
    Stack = []
    for bracket in s:
        if bracket == "(":
            Stack.append(bracket)
        else:
            if Stack and Stack[-1] == "("  and bracket == ")":
                Stack.pop()
            else:
                Stack.append(bracket)
    return len(Stack)

s = "((("
print(minimum_length(s))