# def subarray_product(arr , k):
#     if k <= 1:
#         return 0
#     n = len(arr)
#     product_count = 0
#     for i in range(n):
#         product = 1
#         for j in range(i , n):
#             product *= arr[j]
#             if product >= k:
#                 break
#             product_count += 1
#     return product_count

def subarray_product(arr , k):
    n = len(arr)
    left = 0
    max_count = 0
    product = 1
    for right in range(n):
        product *= arr[right]
        while product >= k:
            product //= arr[left]
            left += 1
        max_count += right - left + 1
    return max_count

arr = [10 , 5 , 2 , 6]
print(subarray_product(arr, 100))