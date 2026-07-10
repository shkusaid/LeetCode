# ____________________ BRUTE FORCE APPROACH __________________

# def speed(piles , h):
#     low = 1
#     high = max(piles)
#     for k in range(low , high + 1):
#         hours = 0
#         for p in piles:
#             hours += (p + k - 1) // k
#         if hours <= h:
#             return k

# __________________________ OPTIMAL SOLUTION ________________________

def speed(piles , h):
    def can_eat(piles , h , k):
        hours = 0
        for p in piles:
            hours += (p + k - 1) // k
        return hours <= h
    low = 1
    high = ans = max(piles)
    while low <= high:
        mid = low + ((high - low) // 2)
        if can_eat(piles , h, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
piles = [3 , 6 , 7 , 11]
print(speed(piles , 8))