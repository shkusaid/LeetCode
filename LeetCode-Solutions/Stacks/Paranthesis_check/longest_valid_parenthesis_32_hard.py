# __________________________ BRUTE FORCE APPROACH __________________________

# def longest_valid_paranthesis(s):
#     Stack = []
#     n = len(s)
#     max_length = 0
#     def is_valid(s , i , j):
#         count = 0
#         for braces in range(i , j + 1):

#             if s[braces] == "(":
#                 count += 1
#             else:
#                 count -= 1
#                 if count < 0:
#                     return False
#         return count == 0
#     for i in range(n):
#         for j in range(i , n):
#             if is_valid(s , i , j):
#                 max_length = max(max_length , j - i + 1)
#     return max_length

# s = ")()())"
# print(longest_valid_paranthesis(s))

def longest_valid_paranthesis(s):
    Stack = [-1]
    length = 0
    for i , ch in enumerate(s):
        if ch == "(":
            Stack.append(i)
        else:
            Stack.pop()
            if not Stack:
                Stack.append(i)
            else:
                length = max(length , i - Stack[-1])
    return length

s = ")()())"
print(longest_valid_paranthesis(s))