
# ______________________ BRUTE FORCE APPROACH _______________

# def permutation(s1 , s2):
#     n = len(s1)
#     m = len(s2)
#     if n > m:
#         return False
#     map_s1 = {}
#     for i in range(n):
#         map_s1[s1[i]] = map_s1.get(s1[i], 0) + 1
#     for i in range(m-n+1):
#         window = {}
#         for j in range(i ,i+n):
#             window[s2[j]] = window.get(s2[j], 0) + 1
#             if window == map_s1:
#                 return True
#     return False


# ____________________ OPTIMAL APPROACH _______________________

def permutation(s1 , s2):
    n = len(s1)
    m = len(s2)
    s1_map = {}
    for i in range(n):
        s1_map[s1[i]] = s1_map.get(s1[i] , 0) + 1

    left = 0
    window = {}
    for right in range(m):
        window[s2[right]] = window.get(s2[right] , 0) + 1
        while right - left + 1 > n:
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]
            left += 1
        if right - left + 1 and window == s1_map:
            return True
    return False

s1 = 'ab'  
s2 = 'eidabooo'
print(permutation(s1 , s2))