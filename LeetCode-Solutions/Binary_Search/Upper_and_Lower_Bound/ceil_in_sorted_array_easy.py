def ceil(nums, target):
    left = 0
    right = len(nums) - 1
    ans = -1
    while left <= right:
        mid = left + ((right - left) // 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

nums = [1, 2, 8, 10 ,12 ,19]
print(ceil(nums, 29))