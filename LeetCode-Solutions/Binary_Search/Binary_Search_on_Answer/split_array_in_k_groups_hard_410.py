# ____________________ BRUTE FORCE APPROACH _________________________

# def split_array_in_group(nums , k):
#     def partition(nums , k , val):
#         current = 0
#         group = 1
#         for num in nums:
#             if current + num <= val:
#                 current += num
#             else:
#                 group += 1
#                 current = num
#         return group <= k 
#     low = max(nums)
#     high = sum(nums)
#     max_ans = high
#     for i in range(low , high + 1):
#         if partition(nums , k , i):
#             max_ans = i
#             return max_ans
#     return max_ans

# ___________________________ OPTIMAL SOLUTION ________________________

def split_array_in_group(nums , k):
    def can_split(nums , k , val):
        count , current = 1 , 0
        for num in nums:
            if current + num <= val:
                current += num
            else:
                count += 1
                current = num
        return count <= k
    low  , high = max(nums) , sum(nums)
    ans = 0
    while low <= high:
        mid = low + (high - low) // 2
        if can_split(nums , k , mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


nums = [7,2,5,10,8]
k = 2
print(split_array_in_group(nums , k))
#output is 18 i.e 10+8 is max of 7+2+5