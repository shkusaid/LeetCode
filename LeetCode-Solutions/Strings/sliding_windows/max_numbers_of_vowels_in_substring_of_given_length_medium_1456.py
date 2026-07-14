def max_vowels(s ,k):
    vowels = {"a" , "e" , "i" , "o" , "u"}
    left = 0
    vowel_char = 0
    for right in range(k):
        if s[right] in vowels:
            vowel_char += 1
    max_vowels_length = vowel_char

    for right in range(k , len(s)):
        if s[right] in vowels:
            vowel_char += 1
        if s[left] in vowels:
            vowel_char -= 1
        left += 1
        max_vowels_length = max(max_vowels_length , vowel_char)
    return max_vowels_length

s = "abciiidef"
print(max_vowels(s , 3))