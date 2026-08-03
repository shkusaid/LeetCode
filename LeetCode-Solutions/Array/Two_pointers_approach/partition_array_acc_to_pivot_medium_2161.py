# def partition(nums , val):
#     count_less= 0
#     count_equal= 0

#     for num in nums:
#         if num < val:
#             count_less += 1
#         elif num == val:
#             count_equal += 1
#     i = 0
#     j = count_less
#     k = count_less + count_equal
#     for num in nums[:]:
#         if num > val:
#             nums[k] = num
#             k += 1
#         elif num == val:
#             nums[j] = num
#             j += 1
#         else:
#             nums[i] = num
#             i += 1
#     return nums

# nums = [3, 2, 2, 1, 4, 5, 2]
# print(partition(nums, 2))  # Output: [1, 2, 2, 2, 3, 4, 5]

# ______________________ Dutch National Flag Algorithm ______________________
# def partition(nums , val):
#     low = 0
#     mid = 0
#     high = len(nums) - 1
#     while mid <= high:
#         if nums[mid] < val:
#             nums[low] , nums[mid] = nums[mid] , nums[low]
#             low+= 1
#             mid += 1
#         elif nums[mid] == val:
#             mid += 1
#         else:
#             nums[high] , nums[mid] = nums[mid] , nums[high]
#             high -= 1
#     return nums

# nums = [9,12,5,10,14,3,10]
# print(partition(nums, 10))  # Output: [9, 5, 3, 10, 10, 12, 14]

# ______________________ Extra Space Approach ______________________
def partition(nums , pivot):
    less = []
    equal = []
    greater = []
    for num in nums:
        if num == pivot:
            equal.append(num)
        elif num < pivot:
            less.append(num)
        else:
            greater.append(num)
    return less + equal + greater

nums = [9,12,5,10,14,3,10]
print(partition(nums, 10))  # Output: [9, 5, 3, 10, 10, 12, 14]