def removing_stars(s):
    Stack = []
    for ch in s:
        if ch =="*":
            Stack.pop()
        else:
            Stack.append(ch)
    return "".join(Stack)

s = "leet**cod*e"
print(removing_stars(s))