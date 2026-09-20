def max_score_after_split(s):
    n = len(s)
    ones = s.count('1')
    max_score = zeros = 0
    for ch in s:
        if ch == '0':
            zeros += 1
        else:
            ones -= 1
        max_score = max(max_score , ones + zeros)
    return max_score
s = '011101'
print(max_score_after_split(s))