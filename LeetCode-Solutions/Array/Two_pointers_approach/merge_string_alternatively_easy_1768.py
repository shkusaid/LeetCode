def merge(w1 , w2):
    n = len(w1)
    m = len(w2)
    i = j = 0
    ans = []
    while i < n and j < m:
        ans.append(w1[i])
        ans.append(w2[j])
        i += 1
        j += 1
    while i < n:
        ans.append(w1[i])
        i += 1
    while j < m:
        ans.append(w1[j])
        j += 1
    return "".join(ans)

w1 = "ace"
w2 = "bdf"

print(merge(w1 , w2))