def subarray(nums):
    subarray_map = {0 : -1}
    ans = 0
    prefix = 0
    for i, num in enumerate(nums):
        if num == 0:
            prefix -= 1
        else:
            prefix += 1
        if prefix in subarray_map:
            ans = max(ans , i - subarray_map[prefix])
        else:
            subarray_map[prefix] = i
    return ans

nums = [0,1,1,0]
print(subarray(nums))