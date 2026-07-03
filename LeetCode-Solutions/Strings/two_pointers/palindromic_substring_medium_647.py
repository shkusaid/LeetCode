

# ______________________________ BRUTE FORCE APPROACHES _____________________


# ________________ BY GIVING LEFT RIGHT AS I AND J TO INNER FUNCTION _________________

# def palindromic_substring(s):
#     def is_palindrome(s , left , right):
#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True
#     n = len(s)
#     count = 0
#     for i in range(n):
#         for j in range(i ,n):
#             if is_palindrome(s , i , j):
#                 count += 1
#     return count

# _________________ CALCULATING LEFT AND RIGHT IN INNER FUNCTION _______________

# def palindromic_substring(s):
#     def is_palindrome(sub):
#         left = 0
#         right = len(sub) - 1
#         while left < right:
#             if sub[left] != sub[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True
#     n = len(s)
#     count = 0
#     for i in range(n):
#         sub = ''
#         for j in range(i ,n):
#             sub += s[j]
#             if is_palindrome(sub):
#                 count += 1
#     return count


# ______________________ OPTIMAL APPROACH ________________________

def palindromic_substring(s):
    def expand(s , left , right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    count = 0
    for i in range(len(s)):
        count += expand(s , i , i)
        count += expand(s , i , i + 1)
    return count




s = 'aaa'
print(palindromic_substring(s))