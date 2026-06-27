def remove_duplicates(arr):
    n = len(arr)
    i = 0
    j = 1
    while j < n:
        if arr[i] != arr[j]:
            i+=1
        arr[i] = arr[j]
        j+=1

arr = [0,0,1,1,2,2,3,3,4]
remove_duplicates(arr)
print(arr)
