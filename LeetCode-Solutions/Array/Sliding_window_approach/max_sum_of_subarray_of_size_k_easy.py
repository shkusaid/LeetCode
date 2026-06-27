def max_sum(arr , k):
    n = len(arr)
    window_sum = 0
    for i in range(k):
        window_sum+=arr[i]
    maxSum = window_sum
    for i in range(k, n):
        window_sum += arr[i]
        window_sum -= arr[i-k]
        maxSum = max(window_sum, maxSum)
    return maxSum

arr = [ 2, 5, 10 , 11, 23, 0 , 19 , 12]
print(max_sum(arr, 4))
        