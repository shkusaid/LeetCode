def three_sum(arr):
    arr.sort()
    n = len(arr)
    result = []
    for i in range(n-2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        j = i+1
        k = n-1
        while j < k:
            sum = arr[i] + arr[j] + arr[k]
            if sum == 0:
                result.append([arr[i],arr[j],arr[k]])
                while j < k and arr[j] == arr[j+1]:
                    j+=1
                while j < k and arr[k] == arr[k-1]:
                    k-=1
                j+=1
                k-=1
            elif sum > 0:
                k-=1
            else:
                j+=1
    return result
arr = [-1, -1, -1, 0, 0, 0, 1, 2, 3]
print(three_sum(arr))
