def floor(nums  , target):
    left = 0
    right = len(nums) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
        
    return ans

nums =[1, 2, 8, 10 , 12]
print(floor(nums , 9))