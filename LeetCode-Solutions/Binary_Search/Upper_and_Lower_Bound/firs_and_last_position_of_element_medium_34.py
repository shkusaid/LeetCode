def first_and_last_occurance(nums , target):
    def find_first(nums , target):
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                ans = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans
    def find_last(nums , target):
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                ans = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return ans
    first = find_first(nums , target)
    last = find_last(nums , target)
    return [first , last]

nums = [ 5, 6, 7, 8, 8, 9, 10]
print(first_and_last_occurance(nums, 8))