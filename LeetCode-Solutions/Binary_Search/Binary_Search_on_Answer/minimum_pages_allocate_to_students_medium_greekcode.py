# _________________ BRUTE FORCE APPROACH __________________________

# def minimum_pages(pages, k):
#     def can_distribute(pages, k, subarray_sum):
#         current = 0
#         group = 1
#         for page in pages:
#             if current + page <= subarray_sum:
#                 current += page
#             else:
#                 group += 1
#                 current = page
#         return group <= k
#     low, high = max(pages), sum(pages)
#     for i in range(low, high + 1):
#         if can_distribute(pages, k, i):
#             return i
#     return low

# ______________________ OPTIMAL SOLUTION _________________________

def minimum_pages(pages , k):
    def can_distribute(pages , k , subarray_sum):
        current = 0 #stores sum of subarray for distribution
        group = 1 #if we initialize with 0 we'll miss first group
        for page in pages:
            if current + page <= subarray_sum:
                current += page
            else:
                group += 1
                current = page
        return group <= k # if gorup is more than k i.e 2 > 3 then it will return False
    low , high = max(pages) , sum(pages) # if k is 1 then all pages should be allocate to 1 student
    # thats why high is sum of array ans low is max bcz weather minimum pages assign to a student is
    # minimum of array or max of array? ofcource maximum
    ans = 0
    while low <= high:
        mid = low + (high - low) // 2
        if can_distribute(pages , k , mid):
            ans = mid
            high = mid -1 # search on left half cz we are looking for minimum possible value
        else:
            low = mid + 1
    return ans

pages = [12 , 34 , 67 , 90]
print(minimum_pages(pages , 2)) # output is 113 (cz 12 + 34 + 67 = 113)