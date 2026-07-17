def next_greater(nums1 , nums2):
    Stack = []
    next_greater_element = {}
    for num in nums2:
        while Stack and num > Stack[-1]:
            next_greater_element[Stack.pop()] = num
        Stack.append(num)
    while Stack:
        next_greater_element[Stack.pop()] = -1
    ans = []
    for num in nums1:
        ans.append(next_greater_element[num])
    return ans

nums1 = [4,1,2] 
nums2 = [1,3,4,2]
print(next_greater(nums1 , nums2))