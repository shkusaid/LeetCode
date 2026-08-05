def counting(allowed , words):
    consist = set(allowed)
    max_count = 0
    for word in words:
        if all(ch in consist for ch in word):
            max_count += 1
    return max_count

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(counting(allowed , words))