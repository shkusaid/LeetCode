# _______________________ BRUTE FORCE APPROACH ________________________

# def magnetic_force(position , m):
#     position.sort()
#     def distance(position , m, gap):
#         count = 1
#         last = position[0]
#         for i in range(1 , len(position)):
#             if position[i] - last >= gap:
#                 count += 1
#                 last = position[i]
#         return count >= m
#     low , high = 1, max(position) - min(position)
#     ans = 0
#     for gap in range(low , high + 1):
#         if distance(position , m , gap):
#             ans = gap
#         else:
#             return ans
#     return ans

# ______________________ OPTIMAL SOLUTION ________________________

def magnetic_force(position , m):
    position.sort()
    def distance(position , m , gap):
        count , last = 1 , position[0]
        for i in range(1 ,len(position)):
            if position[i] - last >= gap:
                count += 1
                last = position[i]
        return count >= m
    low = 1
    high = position[-1] - position[0]
    ans = 0
    while low <= high:
        mid = low + (high - low) // 2
        if distance(position , m , mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

position = [1, 2, 3, 4, 7]
print(magnetic_force(position , 3))