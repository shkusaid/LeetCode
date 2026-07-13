def majority(nums):
    majority_element = nums[0]
    count = 1
    for i in range(1 , len(nums)):
        if count == 0:
            majority_element = nums[i]
            count = 1
        elif nums[i] != majority_element:
            count -= 1
        else:
            count += 1
    return majority_element

nums = [3]
print(majority(nums))