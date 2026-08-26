def beautiful_string(s , k):
    n = len(s)
    left = ones = 0
    ans = ''
    for right in range(n):
        if s[right] == '1':
            ones += 1
        while ones > k:
            if s[left] == '1':
                ones -= 1
            left += 1
        if ones == k:
            while s[left] == '0':
                left += 1
            curr = s[left : right + 1]

            if not ans or len(curr) < len(ans) or (len(ans) == len(curr) and curr < ans):
                ans = curr
    return ans

s = '10001101'
print(beautiful_string(s , 3))