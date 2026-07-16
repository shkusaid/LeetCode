def longest_rectangle(hist):
    n = len(hist)
    max_ans = 0
    for i in range(n):
        height = hist[i]
        for j in range(i,n):
            height = min(height , hist[j])
            width = j - i + 1
            ans = height * width
            max_ans = max(max_ans , ans)
    return max_ans

hist = [2, 1, 5, 6, 2, 3]
print(longest_rectangle(hist))