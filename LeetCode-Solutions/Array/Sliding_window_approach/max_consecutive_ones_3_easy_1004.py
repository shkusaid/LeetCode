# This is the Brute Force Approach Outer Loop will run n times and inner can also
# def max_ones(arr , k):
#     n = len(arr)
#     max_count = 0
#     for i in range(n):
#         count_zero = 0
#         for j in range(i, n):
#             if arr[j] == 0:
#                 count_zero+=1
#             if count_zero > k :
#                 break
#             max_count = max(max_count , j - i + 1)
#     return max_count


# Optimal Solution For This Problem is By Sliding Windows
def max_ones(arr , k):
    n = len(arr)
    left = 0
    max_count = count_zero = 0
    for right in range(n):
        if arr[right] == 0:
            count_zero += 1
        while count_zero > k:
            if arr[left] == 0:
                count_zero-= 1
            left += 1
        max_count = max(max_count, right - left + 1)
    return max_count
        
arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0]
print(max_ones(arr , 2))