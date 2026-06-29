def pivot(arr):
    n = len(arr)
    left_sum = 0
    total_sum = sum(arr)

    for i in range(n):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1
      
arr = [2 , 1,-1]
print(pivot(arr))