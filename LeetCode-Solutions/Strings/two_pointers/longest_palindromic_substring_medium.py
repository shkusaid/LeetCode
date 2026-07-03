
# ________________________ BRUTE FORCE APPROACH __________________________

# def longest_palindrom(s):
#     def is_palindrome(s , left , right):
#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True
#     n = len(s)
#     resultant = ''
#     for i in range(n):
#         for j in range( i , n ):
#             if is_palindrome(s , i , j):
#                 if j  - i + 1 > len(resultant):
#                     resultant = s[i:j+1]
#     return resultant

# ___________________________ OPTIMAL APPROACH _________________________

def longest_palindrom(s):
    def expand(s , left , right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    start = end = 0
    for i in range(len(s)):
        odd = expand(s , i , i)
        even = expand(s , i , i + 1)
        length = max(even , odd)
        if length > end - start:
            end = i + length // 2
            start = i - (length - 1) // 2
    return s[start:end + 1]



s = 'aracecar'
print(longest_palindrom(s))