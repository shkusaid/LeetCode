# bitwise longest xor substring

def substring(nums):
    total = 0
    non_zero = False
    for num in nums:
        if num > 0:
            non_zero = True
            total ^= num
    if not non_zero:
        return 0
    if total != 0:
        return len(nums)
    return len(nums) - 1

nums = [1, 2, 3]
result = substring(nums)
print(result)  # Output: 2
    