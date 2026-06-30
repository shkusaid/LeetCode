# _______________________BRUTE FORCE APPROACH ___________________

# def subarray_sum_multiple_of_k(arr , k):
#     n = len(arr)
#     for i in range(n-1):
#         sum = arr[i]
#         for j in range(i + 1 , n):
#             sum += arr[j]
#             if sum % k == 0:
#                 return True
        
#     return False


# _______________________ OPTIMAL APPROACH ____________________________

def subarray_sum_multiple_of_k(arr , k):
    prefix_sum = 0
    rem_map = {0:-1}
    for i in range(len(arr)):
        prefix_sum += arr[i]
        rem = prefix_sum % k
        if rem in rem_map:
            if i - rem_map[rem] >= 2:
                return True
        else:
            rem_map[rem] = i
    return False
arr = [23, 4, 2, 6, 7]
print(subarray_sum_multiple_of_k(arr , 6))