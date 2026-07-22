# ______________________ BRUTE FORCE APPROACH _________________

# def valid_paranthesis(s):
#     i = 0
#     while i < len(s) - 1:
#         a = s[i]
#         b = s[i + 1]

#         if (a == "(" and b == ")") or (a == "{" and b == "}") or (a == "[" and b == "]"):
#             s = s[:i] + s[i + 2:]
#             if i > 0:
#                 i -= 1
#         else:
#             i += 1
#     return len(s) == 0

# ______________________ OPTIMAL SOLUTION _____________________

def valid_paranthesis(s):
    Stack = []
    for bracket in s:
        if bracket == "(" or bracket == "{" or bracket == "[":
            Stack.append(bracket)
        else:
            if not Stack:
                return False
            if (Stack[-1] == "(" and bracket == ")") or (Stack[-1] == "{" and bracket == "}") or (Stack[-1] == "[" and bracket == "]"):
                Stack.pop()
            else:
                return False
    return len(Stack) == 0

print(valid_paranthesis("((()))"))   # True
print(valid_paranthesis("()[]{}"))   # True
print(valid_paranthesis("(]"))       # False
print(valid_paranthesis("([)]"))     # False
print(valid_paranthesis("{[]}"))     # True


# ___________________ USING DICTIONARY ______________
# def valid_paranthesis(s):
#     Stack = []
#     pairs = {
#         ")": "(",
#         "}" : "{",
#         "]" : "["
#     }

#     for ch in s:
#         if ch in "({[":
#             Stack.append(ch)
#         else:
#             if not Stack and Stack[-1] != pairs[ch]:
#                 return False
#             Stack.pop()
#     return not Stack