
# _______________________ BRUTE FORCE CODE ____________________________

# import time
# def anagrams(s , p):
#     start = time.time()
#     res = []
#     n = len(s)
#     k = len(p)
#     p_count = [0] * 26 # as alphabets are 26
#     for ch in p:
#         p_count[ord(ch) - ord('a')] += 1 # ASCII to Number conversion
    
#     for i in range( n - k + 1 ):
#         s_count = [0] * 26
#         for j in range(i , i + k):
#             s_count[ord(s[j]) - ord('a')] += 1
#         if p_count == s_count:
#             res.append(i)
#     end = time.time()
#     print("Total Time taken is: ", (end - start) * 1000 , " miliseconds")
#     return res

# s = "cbaebabacd"
# p = 'abc'
# print(anagrams(s , p))


# ________________________ OPTIMAL APPROACH ______________________

# ______________ 2 HASH TABLES ____________________(using count variable)

# def anagrams(s , p):
#     if len(s) < len(p):
#         return []
#     res = []
#     p_map = {}
#     s_map = {}
#     for ch in p:
#         if ch in p_map:
#             p_map[ch] += 1
#         else:
#             p_map[ch] = 1
#     count = len(p)
#     left = 0
#     for right in range(len(s)):
#         ch = s[right]
#         if ch in s_map:
#             s_map[ch] += 1
#         else:
#             s_map[ch] = 1
#         if ch in p_map and s_map[ch] <= p_map[ch]:
#             count -= 1
#         if right - left + 1 > len(p):
#             left_char = s[left]
#             if left_char in p_map and s_map[left_char] <= p_map[left_char]:
#                 count += 1
#             s_map[left_char] -= 1
#             if s_map[left_char] == 0:
#                 del s_map[left_char]
#             left += 1
#         if count == 0:
#             res.append(left)
#     return res

# __________________ 2 HASH TABLE _______________(comparing both tables every window)

def anagrams(s , p):
    res = []
    p_map = {}
    s_map = {}
    for ch in p: # creating hash table of p (p_map) an insering elements
        if ch in p_map:
            p_map[ch] += 1
        else:
            p_map[ch] = 1
    
    for i in range(len(p)): # insering p elements of s in s_map
        if s[i] in s_map:
            s_map[s[i]] += 1
        else:
            s_map[s[i]] = 1
    if p_map == s_map: # Comparing 1st window with p
        res.append(0)
    for i in range(len(p) , len(s)): # Slide the Window
        if s[i] in s_map:
            s_map[s[i]] += 1
        else:
            s_map[s[i]] = 1
        
        left_char = s[i - len(p)]
        s_map[left_char] -= 1
        if s_map[left_char] == 0:
            del s_map[left_char]
        if s_map == p_map:
            res.append(i - len(p) + 1)
    return res



s = "cbaebabacd"
p = 'abc'
print(anagrams(s , p))