def move_zeros(arr):
    n = len(arr)
    i = 0
    j = 0
    while j < n:
        if arr[j] != 0:
            arr[i] , arr[j] = arr[j] , arr[i]
            i+=1
        j+=1

arr = [0, 0, 0, 12, 0, 0]
move_zeros(arr)
print(arr)