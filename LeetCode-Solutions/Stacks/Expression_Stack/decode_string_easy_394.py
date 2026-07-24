def decode_string(s):
    Stack = []
    for ch in s:
        if ch != "]":
            Stack.append(ch)
        else:
            string = []
            while Stack[-1] != "[":
                string.append(Stack.pop())
            string.reverse()
            Stack.pop()
            num = []
            while Stack and Stack[-1].isdigit():
                num.append(Stack.pop())
            num.reverse()
            repeat = int("".join(num))
            Stack.extend(string * repeat)
    return "".join(Stack)


s = "2[abc]3[cd]ef"
print(decode_string(s))