def greatest_number_of_letter(s):
    appearance = set(s)
    for ch in "ZYXWVUTSRQPONMLKJIHGFEDCBA":
        if ch in appearance and ch.lower() in appearance:
            return ch
    return ""

s = "adD"
print(greatest_number_of_letter(s))