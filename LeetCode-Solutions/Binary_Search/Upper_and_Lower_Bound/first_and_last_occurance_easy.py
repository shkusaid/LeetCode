def occurance(nums , target):    
    def first(nums, target):
        ans = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                ans = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
    def last(nums, target):
        ans = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                ans = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans
    left = first(nums , target)
    right = last(nums , target)
    return 0 if left == -1 else right - left + 1

nums = [1,1,2,2,2,2,3]
print(occurance(nums , 4))