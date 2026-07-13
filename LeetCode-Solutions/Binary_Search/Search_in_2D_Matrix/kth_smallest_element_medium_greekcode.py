# # __________________ BRUTE FORCE APPROACH ____________________
# def kth_smallest(mat , k):
#     def is_small(mat , k , target):
#         r = n -1
#         c = count = 0
#         while r >=0 and c < n:
#             if mat[r][c] <= target:
#                 count += r + 1
#                 c += 1
#             else:
#                  r -= 1
#         return count >= k

#     n = len(mat)
#     low = mat[0][0]
#     high = mat[-1][-1]
#     for val in range(low , high + 1):
#         if is_small(mat , k , val):
#             return val
#     return -1

# mat = [[16 , 17 , 35 , 64] , [18, 41, 63, 91] , [27 , 50 , 87, 93] , [36 , 78 , 87 , 94]]
# print(kth_smallest(mat , 3))

# ______________________ OPTIMAL SOLUTION _________________________

def kth_smallest(mat , k):
    def is_small(mat , k , target):
        r = n -1
        c = count = 0
        while r >=0 and c < n:
            if mat[r][c] <= target:
                count += r + 1
                c += 1
            else:
                 r -= 1
        return count >= k
    n = len(mat)
    low = mat[0][0]
    high = mat[-1][-1]
    ans = -1
    while low <= high:
        val = low + (high - low) // 2
        if is_small(mat , k , val):
            ans = val
            high = val - 1
        else:
            low = val + 1
    return ans
mat = [[16 , 17 , 35 , 64] , [18, 41, 63, 91] , [27 , 50 , 87, 93] , [36 , 78 , 87 , 94]]
print(kth_smallest(mat , 3))