def max_average(arr , k):
    n = len(arr)
    window_sum = 0
    for i in range(k):
        window_sum += arr[i]
    maximum_sum = window_sum 
    for j in range(k , n):
        window_sum += arr[j]
        window_sum -= arr[j-k]
        maximum_sum = max(maximum_sum , window_sum)
    return maximum_sum / k

arr = [1,12,-5,-6,50,3]
print(max_average(arr ,4))