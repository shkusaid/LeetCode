# ____________________________ Complex Code _________________________________
from math import gcd
# def common_divisor(nums):
#     largest = smallest = nums[0]
#     for num in nums:
#         if num > largest:
#             largest = num
#         elif num < smallest:
#             smallest = num
#     return gcd(largest , smallest)

def common_divisor(nums):
    return gcd(max(nums) , min(nums))
nums = [7,5,6,8,3]
print(common_divisor(nums))
    