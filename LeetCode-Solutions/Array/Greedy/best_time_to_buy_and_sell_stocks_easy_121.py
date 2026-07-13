def buy_and_sell(nums):
    max_profit = 0
    l = 0
    for r in range(1 , len(nums)):
        if nums[r] > nums[l]:
            max_profit = max(max_profit , nums[r] - nums[l])
        else:
            l = r
    return max_profit

nums = [7,1,5,3,6,4]
print(buy_and_sell(nums))