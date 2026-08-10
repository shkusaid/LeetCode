def two_sum(nums, target):
    freq = {}
    for i , num in enumerate(nums):
        complement = target - num
        if complement in freq:
            return [freq[complement] , i]
        freq[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
if result:
    print(f"Indices of the two numbers that add up to {target} are: {result}")