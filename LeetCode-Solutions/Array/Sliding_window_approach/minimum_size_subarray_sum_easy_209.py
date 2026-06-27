def min_subarray(nums , target):
        sum = 0
        size = float('inf')
        left = 0
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                size = min(size , right - left + 1)
                sum -= nums[left]
                left += 1
        return 0 if size == float('inf') else size


arr = [2, 3, 2, 2, 4, 3]
print(min_subarray(arr , 7))
