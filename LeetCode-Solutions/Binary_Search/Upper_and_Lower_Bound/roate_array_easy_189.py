# _____________________ BRUTE FORCE APPROACH (as T.C is O(n ^ 2)) ________________

# def rotate(nums , k):
#     n = len(nums)
#     k %=n
#     for _ in range(k):
#         temp = nums[n - 1]
#         for j in range(n-2 , -1, -1):
#             nums[j+1] = nums[j]
#         nums[0] = temp
#     return nums


# ___________________ OPTIMAL SOLUTION ___________ (T.C is O(n) alng with S.C O(n)) _________

# def rotate(nums , k):
#     n = len(nums)
#     temp = [0] * n
#     for i in range(n):
#         temp[i] = nums[i]
    
#     for i in range(n):
#         nums[(i + k) % n] = temp[i]
#     return nums

def rotate(nums , k):
    n = len(nums)
    k %= n
    def reverse(left , right):
        while left < right:
            nums[left] , nums[right] = nums[right] , nums[left]
            left += 1
            right -= 1
    reverse( 0 , n - 1 )
    reverse( 0 , k - 1 )
    reverse( k , n - 1 )

# ___________________ This can also _______________
    # nums.reverse()
    # nums[:k] = reversed(nums[:k])
    # nums[k:] = reversed(nums[k:])

# _________________________________________________
    return nums

nums=[1,2,3,4,5,6,7]
print(rotate(nums , 3))