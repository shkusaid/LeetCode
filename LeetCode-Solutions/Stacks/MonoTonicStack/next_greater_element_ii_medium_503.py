def next_greater_element(nums):
    n = len(nums)
    ans = [-1] * n
    Stack = []
    for i in range(2 * n - 1, -1, -1):
        num = nums[i % n]
        while Stack and Stack[-1] <= num:
            Stack.pop()
        if i < n and Stack:
            ans[i] = Stack[-1]
        Stack.append(num)
    return ans

nums = [1 , 2, 1]
print(next_greater_element(nums))