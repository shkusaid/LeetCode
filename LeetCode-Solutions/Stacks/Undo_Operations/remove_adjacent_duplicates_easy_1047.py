def remove_adjacent(s):
    Stack = []
    for ch in s:
        if Stack and Stack[-1] == ch:
            Stack.pop()
        else:
            Stack.append(ch)
    return "".join(Stack)

s = "abbaca"
print(remove_adjacent(s))