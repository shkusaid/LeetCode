def reverse_string(arr):
    n = len(arr)
    left = 0
    right = n - 1

    while left < right:
        arr[left] , arr[right] = arr[right] , arr[left]
        left += 1
        right -= 1
    return arr

s = ["H","a","n","n","a","h"]
print(reverse_string(s))