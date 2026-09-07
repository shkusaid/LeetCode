def heights_check(heights):
    count = [0] * 101
    for h in heights:
        count[h] += 1
    ans = expected = 0
    for h in heights:
        while count[expected] == 0:
            expected += 1
        if h != expected:
            ans += 1
        count[expected] -= 1
    return ans

heights = [1, 1, 4, 2, 1, 3]
print(heights_check(heights))