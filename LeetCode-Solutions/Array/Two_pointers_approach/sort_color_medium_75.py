def sort_colors(arr):
    l = m =0
    h = len(arr) - 1
    while m <= h:
        if arr[m] == 0:
            arr[l] , arr[m] = arr[m] , arr[l]
            m+=1
            l+=1
        elif arr[m] == 2:
            arr[h] , arr[m] = arr[m] , arr[h]
            h-=1
        else:
            m+=1

arr = [2, 1, 2, 0, 0 , 2]
sort_colors(arr)
print(arr)