def remove_same_values(s):
    i , j = 0 , len(s) - 1
    while i < j and s[i] == s[j]:
        ch = s[i]
        while i <= j and s[i] == ch:
            i += 1
        while i <= j and s[j] == ch:
            j -= 1
    return j - i + 1

s = 'aabcaabba'
print(remove_same_values(s))