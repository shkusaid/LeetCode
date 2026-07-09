def search_in_2d(nums , target):
    n = len(nums)
    top = 0
    bottom = n - 1
    while top <= bottom:
        center = top + (bottom - top ) // 2
        if nums[center][0] <= target and  nums[center][-1] >= target:
            l = 0
            r = len(nums[0]) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[center][m] == target:
                    return True
                elif nums[center][m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return False
        elif nums[center][0] > target:
            bottom = center - 1
        else:
            top = center + 1
    return False

nums = [[1,3,5,7] , [10 , 11, 16 , 20] , [23, 30 , 34, 60]]
print(search_in_2d(nums , 3))