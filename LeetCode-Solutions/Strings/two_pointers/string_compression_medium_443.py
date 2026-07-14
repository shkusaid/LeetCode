# ____________ This is not modifying actual chars instead we've to optimize chars _________

# def string_compression(chars):
#     left = 0
#     output = ""
#     n = len(chars)
#     if n == 1:
#         return 1
#     for right in range(n):
#         if right == n - 1 or chars[right] != chars[right + 1]:
#             count = right - left + 1
#             output += chars[left]
#             if count > 1:       
#                 output += str(count)
#             left = right + 1
            
#     return len(output)

# chars = ["a","a","b","b","c","c","c"]
# print(string_compression(chars))


# _______________________________ Optimal Solution ___________________________________

def string_compression(chars):
    left = write = 0
    n = len(chars)
    for right in range(n):
        if right == n - 1 or chars[right] != chars[right + 1]:
            count = right - left + 1
            chars[write] = chars[left]
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            left = right + 1
    return write

chars = ["a","a","b","b","c","c","c"]
print(string_compression(chars))