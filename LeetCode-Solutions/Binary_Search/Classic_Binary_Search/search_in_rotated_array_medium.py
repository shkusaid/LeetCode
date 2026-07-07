def rotated_array_search(nums , target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
            if nums[left] <= target and nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and nums[mid] >= target:
                left = mid + 1
            else:
                right = mid - 1
    return -1

nums = [3 ,4, 5, 6, 7, 0, 1, 2]
print(rotated_array_search(nums , 0))