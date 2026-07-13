def four_sum(nums , target):
    nums.sort()
    arr = []
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i  + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total == target:
                    arr.append([nums[i], nums[j], nums[k], nums[l]])
                    while k < l and nums[k] == nums[k + 1]:
                        k += 1
                    while k < l and nums[l] == nums[l - 1]:
                        l -= 1
                    k += 1
                    l -= 1
                elif total > target:
                    l -= 1
                else:
                    k += 1
    return arr

nums = [1,0,-1,0,-2,2]
print(four_sum(nums , 0))