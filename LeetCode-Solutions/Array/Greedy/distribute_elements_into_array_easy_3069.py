def distribute(nums):
    n = len(nums)
    arr1 = [nums[0]]
    arr2 = [nums[1]]
    for i in range(2 , n):
        if arr1[-1] > arr2[-1]:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])
    return arr1 + arr2

nums = [7 , 3, 4, 5]
print(distribute(nums))