# ____________________ BRUTE FORCE APPROACH _______________________
# def max_sum_subarray(arr):
#     n = len(arr)
#     max_sum = arr[0]
#     for i in range(n):
#         sum = 0
#         for j in range(i ,n):
#             sum += arr[j]
#             max_sum = max(max_sum , sum)
#     return max_sum


# _________________ OPTIMAL APPROACH _______________________
            #  CHAT GPT CODE __________
# def max_sum_subarray(arr):
#     max_sum = current_sum = arr[0]
#     for i in range(1 , len(arr)):
#         current_sum = max(arr[i] , current_sum + arr[i])
#         max_sum = max(max_sum , current_sum)
#     return max_sum


            # MINE CODE _______________
def max_sum_subarray(nums):
    current_sum = 0
    max_sum = nums[0]
    for num in nums:
        current_sum += num
        max_sum = max(max_sum , current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sum_subarray(arr))