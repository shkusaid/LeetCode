def remove_duplicates(nums):
    left = 2
    for right in range(2 , len(nums)):
        if nums[left -2]  != nums[right]:
            nums[left] = nums[right]
            left += 1
    
    return nums

nums= [1 ,1,1, 2, 2, 3]
print(remove_duplicates(nums))
