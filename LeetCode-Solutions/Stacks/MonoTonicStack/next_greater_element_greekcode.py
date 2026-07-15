# _____________________ BRUTE FORCE APPROACH __________________________

# def next_greater_element(nums):
#     n = len(nums)
#     ans = []
#     for i in range(n):
#         next_greater = -1
#         for j in range(i + 1 , n):
#             if nums[j] > nums[i]:
#                 next_greater = nums[j]
#                 break
#         ans.append(next_greater)
#     return ans


def next_greater_element(nums):
    Stack = []
    ans = [-1] * len(nums)
    for i in range(len(nums) - 1 , -1 , -1):
        while Stack and Stack[-1] <= nums[i]:
            Stack.pop()
        if Stack:
            ans[i] = Stack[-1]
        Stack.append(nums[i])
    return ans

nums= [4 , 3, 2, 1]
print(next_greater_element(nums))