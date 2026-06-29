def middle(arr):
    left_sum , right_sum = 0 , sum(arr)
    for i in range(len(arr)):
        right_sum -= arr[i]
        if right_sum == left_sum:
            return i
        left_sum += arr[i]
    return -1


arr = [2,5]
print(middle(arr))