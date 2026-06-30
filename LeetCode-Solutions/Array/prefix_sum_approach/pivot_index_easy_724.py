# __________________________ BRUTE FORCE APPROACH ___________________

# def pivot(arr):
#     n = len(arr)
#     for i in range(n):
#         left_sum = 0
#         for j in range(i):
#             left_sum += arr[j]
#         right_sum = 0
#         for k in range(i+1 , n):
#             right_sum += arr[k]
#         if left_sum == right_sum:
#             return i
#     return -1
# __________________________ OPTIMAL APPROACH _______________________

def pivot(arr):
        # ______________ FORWARD ORDER ____________
    # n = len(arr)
    # left_sum = 0
    # total_sum = sum(arr)

    # for i in range(n):
    #     right_sum = total_sum - left_sum - arr[i]
    #     if left_sum == right_sum:
    #         return i
    #     left_sum += arr[i]
    # return -1
        # __________ REVERSE ORDER ___________
    right_sum = 0
    total_sum = sum(arr)
    for left in range(len(arr) - 1 , -1 , -1):
        left_sum = total_sum - right_sum - arr[left]
        if left_sum is right_sum:
            return left
        right_sum += arr[left]
    return -1
      
arr = [1 ,7 ,3, 6, 5, 6]
print(pivot(arr))