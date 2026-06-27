def trapping(arr):
    i = 0
    j = len(arr) - 1
    left_max = 0
    right_max = 0
    water = 0
    while i < j:
        if arr[i] < arr[j]:
            if arr[i] >= left_max:
                left_max = arr[i]
            else:
                water += left_max - arr[i]
            i += 1
        else:
            if arr[j] >= right_max:
                right_max = arr[j]
            else:
                water += right_max - arr[j]
            j-=1
    return water        

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapping(arr))
