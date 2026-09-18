def next_permutations(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i] , nums[j] = nums[j] , nums[i]
    nums[i + 1:] = nums[i + 1:][::-1]
    return nums

nums = [1,2,3]
print(next_permutations(nums))