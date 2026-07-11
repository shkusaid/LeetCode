# # ___________________________ BRUTE FORCE APPROACH ______________________

# def aggressive_cows(stalls , k):
#     stalls.sort()
#     def distance(stalls , k , gap):
#         ans = 0
#         cows = 1
#         last = stalls[0]
#         for i in range(1 , len(stalls)):
#             if stalls[i] - last >= gap:
#                 cows += 1
#                 last = stalls[i]
#         if cows >= k:
#             return True
#         return False
#     low = 1
#     high = max(stalls) - min(stalls)
#     for gap in range(high ,low - 1 , -1):
#         if distance(stalls , k , gap):
#             return gap
#     return low

# stalls = [1 , 2, 4, 8, 9]
# print(aggressive_cows(stalls , 3))

# ___________________________ OPTIMAL APPROACH ______________________
def aggressive_cows(stalls , k):
    stalls.sort()
    def distance(stalls , k , gap):
        ans = 0
        cows = 1
        last = stalls[0]
        for i in range(1 , len(stalls)):
            if stalls[i] - last >= gap:
                cows += 1
                last = stalls[i]
        return cows >= k
    low = 1
    high = max(stalls) - min(stalls)
    ans = 0
    while low <= high:
        gap = low + (high - low ) // 2
        if distance(stalls , k , gap):
            ans = gap
            low = gap + 1
        else:
            high = gap - 1
    return ans
stalls = [1 , 2, 4, 8, 9]
print(aggressive_cows(stalls , 3))