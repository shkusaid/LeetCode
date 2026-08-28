def longest_mountain(arr):
    n = len(arr)
    i , ans = 1 , 0
    while i < n - 1:
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            left = right = i
            while left > 0 and arr[left] > arr[left - 1]:
                left -= 1
            while right + 1 < n and arr[right] > arr[right + 1]:
                right += 1
            ans = max(ans , right - left + 1)
            i = right
        else:
            i += 1
    return ans

arr = [2,1,4,7,3,2,5]
print(longest_mountain(arr))