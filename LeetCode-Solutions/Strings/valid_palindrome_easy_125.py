def isalphanumeric(c):
    return (
        ("a" <= c and c <= "z") or
        ("A" <= c and c <= "Z") or
        ("0" <= c and c <= "9")
    )

def valid_palindrom(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if not isalphanumeric(s[left]): # user-defined function
            left += 1
        elif not s[right].isalnum(): # Built-in function
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    return True


s = "race :a car"
print(valid_palindrom(s))
