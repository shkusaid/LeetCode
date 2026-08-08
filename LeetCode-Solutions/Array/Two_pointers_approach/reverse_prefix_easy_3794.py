def prefix_reverse(s , k):
    # return s[:k][::-1] + s[k:]
    i = 0
    j = k -1
    s = list(s)
    while i < j:
        s[i] , s[j] = s[j] , s[i]
        i += 1
        j -= 1
    return "".join(s)

s = "abcdefgh"
print(prefix_reverse(s, 3))  # Output: "cbadefgh"