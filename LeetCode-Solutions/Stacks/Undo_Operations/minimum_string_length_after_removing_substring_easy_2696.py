def min_length(s):
    Stack = []
    val_A = ord("A")
    val_B = ord("C")
    for ch in s:
        if Stack and ((Stack[-1] == "A" and ch == "B") or (Stack[-1] == "C" and ch == "D")):
            Stack.pop()
        else:
            Stack.append(ch)
    return len(Stack)

s = "ACBBD"
print(min_length(s))