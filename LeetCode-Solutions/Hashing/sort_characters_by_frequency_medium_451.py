def sort_characters(s):
    freq = {}
    ans = ''
    for ch in s:
        freq[ch] = freq.get(ch , 0) + 1

    chars = sorted(freq , key=freq.get , reverse=True)
    for ch in chars:
        ans += ch * freq[ch]
    return ans

s = 'tree'
print(sort_characters(s))