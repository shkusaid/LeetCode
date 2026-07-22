def string_great(s):
    def lower(ch):
        return ch >= "a" and ch <= "z"
    def upper(ch):
        return ch >= "A" and ch <= "Z"
            
    Stack = []
    for ch in s:
        if Stack and abs(ord(Stack[-1]) - ord(ch)) == 32: #abs as sometimes uppercase letter comes
            # first and ord as it returns ASCII code and 32 as difference between upper case and
            # lower case ASCII code is 32
            Stack.pop()
        else:
            Stack.append(ch)
    return "".join(Stack)


s = "leEeetcode"
print(string_great(s))