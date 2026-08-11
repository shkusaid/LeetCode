def three_sum_closest(nums , target):
    nums.sort()
    n = len(nums)
    closest = nums[0] + nums[1] + nums[2]
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(total - target) < abs(closest - target):
                closest = target
            if target < total:
                right -= 1
            elif target > total:
                left += 1
            else:
                return total
    return closest

nums = [-7, 2, 5, -4 , 1]
target = 1
print(three_sum_closest(nums, target))