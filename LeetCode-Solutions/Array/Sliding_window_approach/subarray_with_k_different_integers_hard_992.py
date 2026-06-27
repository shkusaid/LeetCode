# ___________________________ BRUTE FORCE APPROACH _________________________
# def k_integers(arr , k):
#     count = 0
#     for i in range(len(arr)):
#         int_map = {}
#         for j in range(i , len(arr)):
#             int_map[arr[j]]  = int_map.get(arr[j] , 0) + 1
#             if len(int_map) == k:
#                 count += 1
#             elif len(int_map) > k:
#                 break
#     return count


# ___________________________OPTIMAL SOLUTION __________________________
def k_integers(arr , k):
    def at_most(arr , k):
        left = 0
        count = 0
        int_map = {}
        for right in range(len(arr)):
            int_map[arr[right]] = int_map.get(arr[right] , 0) + 1
            while len(int_map) > k:
                int_map[arr[left]] -= 1
                if int_map[arr[left]] == 0:
                    del int_map[arr[left]]
                left += 1
            count += right - left + 1
        return count
    return at_most(arr , k) - at_most(arr , k - 1)
arr = [1, 2, 1, 2, 3]
print(k_integers(arr , 2))