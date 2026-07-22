def score_of_paranthesis(s):
    Stack = [0]
    for ch in s:
        if ch == "(":
            Stack.append(0)
        else:
            val = Stack.pop()
            Stack[-1] += max(val * 2 , 1)
    return Stack[0]

s = "(()(()))"
print(score_of_paranthesis(s))