# ____________________________________ BRUTE FORCE APPROACH __________________
# def subarray_sum(arr , k):
#     count = 0
#     for i in range(len(arr)):
#         sum = 0
#         for j in range(i , len(arr)):
#             sum += arr[j]
#             if sum is k:
#                 count += 1
#     return count

# arr = [1, 2, 3]
# print(subarray_sum(arr , 3))

# ____________________________________ OPTIMAL APPROACH _________________________
# def subarray_sum(nums , k) :
#     freq = {0:1}
#     prefix_sum = 0
#     count = 0
#     for num in nums:
#         prefix_sum += num
#         if prefix_sum - k in freq:
#             count += freq[prefix_sum - k]
#         freq[prefix_sum] = freq.get(prefix_sum , 0) + 1
#     return count

def subarray_sum(nums, k):
    prefix_sum = 0
    k_map = {0:1}
    count = 0
    for num in nums:
        prefix_sum += num

        if prefix_sum - k in k_map:
            count += k_map[prefix_sum - k]
        k_map[prefix_sum] = k_map.get(prefix_sum , 0) + 1
    return count


arr = [1, -1, 0, 1, 2, -1, 3]
print(subarray_sum(arr , 3))