def reverse_polish(tokens):
    n = len(tokens)
    Stack = []
    for ch in tokens:
        if ch.lstrip("-").isdigit():
            Stack.append(int(ch))
        else:
            a = Stack.pop()
            b = Stack.pop()
            if ch == "+":
                Stack.append(a + b)
            elif ch == "-":
                Stack.append(b - a)
            elif ch == "*":
                Stack.append(a * b)
            else:
                Stack.append(int(b / a))
    return Stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(reverse_polish(tokens))