# ________________________ BRUTE FORCE APPROACH __________________________

# def longest_substring_without_repeating(s):
    # n = len(s)
    # max_len = 0
    # for i in range(n):
    #     substring_map = {}
    #     for j in range(i , n):
    #         if s[j] in substring_map:
    #             # max_len = max(max_len , j - i) # if it contains all unique then this will return 0 so it fails
    #             break
    #         substring_map[s[j]] = 1
    #         max_len = max(max_len , j - i + 1)
    # return max_len


# _________________________ OPTIMAL APPROACH _____________________________

def longest_substring_without_repeating(s):
    map = {}
    max_len = 0
    left = 0
    for right in range(len(s)):
        if s[right] in map:
            map[s[right]] += 1
        else:
            map[s[right]] = 1
        while map[s[right]] > 1:
            map[s[left]] -= 1
            if map[s[left]] == 0:
                del map[s[left]]
            left += 1
        max_len = max(max_len , right - left + 1)

    return max_len


s = 'abcabcbb'
print(longest_substring_without_repeating(s))