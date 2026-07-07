def peak(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + ((right - left) // 2)
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
nums = [1,2,1,3,5,6,4]
print(peak(nums))