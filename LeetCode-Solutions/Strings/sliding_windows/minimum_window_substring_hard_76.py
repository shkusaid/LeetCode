# _______________________ BRUTE FORCE APPROACH ______________________

# def minimum_window_substring(s , t):
#     def is_valid(t_map , window):
#         for ch in t_map:
#             if window.get(ch , 0) < t_map[ch]:
#                 return False
#         return True
#     t_map = {}
#     ans = ''
#     for i in range(len(t)):
#         t_map[t[i]] = t_map.get(t[i] , 0) + 1
#     for i in range(len(s)):
#         window = {}
#         for j in range(i , len(s)):
#             window[s[j]] = window.get(s[j] , 0) + 1
#             if is_valid(t_map , window):
#                 sub = s[i:j+1]
#                 if len(sub) < len(ans) or ans == "":
#                     ans = sub
#     return ans

# ___________________________ OPTIMAL SOLUTION _______________________

def minimum_window_substring(s, t):
    t_map = {}
    for ch in t:
        t_map[ch] = t_map.get(ch, 0) + 1

    window = {}
    left = 0
    count = len(t)
    ans = ""

    for right in range(len(s)):
        if s[right] in t_map:
            window[s[right]] = window.get(s[right], 0) + 1
            if window[s[right]] <= t_map[s[right]]:
                count -= 1

        while count == 0:
            sub = s[left:right + 1]
            if ans == "" or len(sub) < len(ans):
                ans = sub
            if s[left] in t_map:
                window[s[left]] -= 1
                if window[s[left]] < t_map[s[left]]:
                    count += 1
                if window[s[left]] == 0:
                    del window[s[left]]
            left += 1

    return ans

           
s = "ADOBECODEBANC"
t = "ABC"

print(minimum_window_substring(s, t))