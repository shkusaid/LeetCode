def valid_pallindrom(x):
    if x < 0 :
        return False
    n = str(x)
    i = 0
    j = len(n) - 1
    if len(n) % 2 == 0:
        while i < j:
            if n[i] != n[j]:
                return False
            i+=1
            j-=1
    else:
        while i != j:
            if n[i] != n[j]:
                return False
            i+=1
            j-=1
    return True
print(valid_pallindrom(1321))