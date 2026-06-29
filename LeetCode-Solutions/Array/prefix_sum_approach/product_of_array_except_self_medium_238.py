# def product_except_self(arr):
#     n = len(arr)
#     left_product = 1
#     right_product = 1
#     answer = [0] * n
#     left_arr = [0] * n
#     right_arr = [0] * n
#     i = 0
#     k = n - 1
#     if i < n:
#         for j in range(i):
#             left_product *= arr[j]
#         left_arr[i] = left_product
#         i+=1
#     if k >= 0:
#         for l in range(n - 1 , k - 1, -1):
#             right_product *= arr[l]
#         right_arr[k] = right_product
#         k-=1
#     for x in range(n):
#         answer[x] = left_arr[x] * right_arr[x]
#     return answer

# arr = [1,2,3,4]
# print(product_except_self(arr))

# _________________________ BRUTE FORCE APPROACH __________________________

# def product_except_self(arr):
#     answer = [0] * len(arr)
#     for i in range(len(arr)):
#         product = 1
#         for j in range(len(arr)):
#             if i == j :
#                 continue
#             product *= arr[j]
#         answer[i] = product
#     return answer

# _________________________OPTIMAL APPROACH ________________________________
def product_except_self(arr):
    n = len(arr)
    answer = [0] * len(arr)
    answer[0] = 1
    right_product = 1
    for left in range(1 , n):
        answer[left] = arr[left - 1] * answer[left - 1]
    for right in range(n-1 , -1 , -1):
        answer[right] = right_product * answer [right]
        right_product *= arr[right]
    return answer

arr = [-1,1,0,3,-3]
print(product_except_self(arr))