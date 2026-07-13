# ______________ T.C is O(m +n) but solve in o(log (m + n)) using binary search _______________

# def median_of_sorted_array(nums1 , nums2):
#     arr = []
#     i = j = 0
#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] < nums2[j]:
#             arr.append(nums1[i])
#             i += 1
#         else:
#             arr.append(nums2[j])
#             j += 1
#     while i < len(nums1):
#         arr.append(nums1[i])
#         i += 1
#     while j < len(nums2):
#         arr.append(nums2[j])
#         j += 1
#     n = len(arr)
#     mid = n // 2
#     if n % 2 != 0:
#         return arr[mid]
#     else:
#         return (arr[mid] + arr[mid-1]) / 2
        
    
# nums1 = [1 , 3]
# nums2 = [2 , 4]
# print(median_of_sorted_array(nums1 , nums2))