def count_commas(n):
    t , ans = 1000 , 0
    while t <= n:
        ans += n - t + 1
        t *= 1000
    return ans

print(count_commas(1002))