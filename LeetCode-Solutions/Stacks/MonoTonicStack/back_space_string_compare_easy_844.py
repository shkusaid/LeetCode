# _________________________ Stack with extra O(n) Space ___________________________

# def back_space_compare(s , t):
#     def is_char(ch):
#         return ch >= "a" and ch <= "z"
#     Stack_s = []
#     Stack_t = []
#     for op in s:
#         if is_char(op):
#             Stack_s.append(op)
#         elif Stack_s:
#             Stack_s.pop()
#     for op in t:
#         if is_char(op):
#             Stack_t.append(op)
#         elif Stack_t:
#             Stack_t.pop()
#     return Stack_t == Stack_s

# _________________________ CONSTANT TWO POINTER SPACE OPTIMAL SOLUTION __________________

def back_space_compare(s , t):
    i = len(s) -1
    j = len(t) -1
    skip_s = skip_t = 0
    while i >= 0 or j >= 0:
        while i >= 0:
            if s[i] == "#":
                skip_s += 1
                i -= 1
            elif skip_s > 0:
                skip_s -= 1
                i-=1
            else:
                break
        while j >= 0:
            if s[j] == "#":
                skip_t += 1
                j -= 1
            elif skip_t > 0:
                skip_t -= 1
                j-=1
            else:
                break
        if i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
        elif i >= 0 or j >= 0:
            return False
        i -= 1
        j -= 1
    return True

s = "a#c"
t = "b"

print(back_space_compare(s , t))
