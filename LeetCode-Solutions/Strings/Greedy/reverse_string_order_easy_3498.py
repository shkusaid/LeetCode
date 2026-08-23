def reverse_string(s):
    total = 0
    for i , ch in enumerate(s):
        total = total + (26 - (ord(ch) - ord('a'))) * (i + 1)
    return total

s = 'zaza'
print(reverse_string(s))