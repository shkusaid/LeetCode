def remove_min_max(nums):
    n = len(nums)
    minimum = nums.index(min(nums))
    maximum = nums.index(max(nums))
    return min(
        max(minimum , maximum) + 1,
        n - min(minimum , maximum),
        maximum + 1 + n - minimum,
        minimum + 1 + n - maximum
    )

nums = [0,-4,19,1,8,-2,-3,5]
print(remove_min_max(nums))