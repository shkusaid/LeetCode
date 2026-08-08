# ______________________ S.C is 0(n)
# def fibonacci(n):
#     arr = [0 , 1]
#     for i in range(2 , n + 1):
#         arr.append(arr[i-1] + arr[i - 2])
#     return arr[n]
# print(fibonacci(8))

# _______________________ T.C is 2 ^ n _____________________
# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(8))

# _______________________ Linear T.C and S.C ______________________
def fibonacci(n):
    if n==1 or n==2:
        return n
    prev0 = 0
    prev1 = 1
    for i in range(2 , n + 1):
        temp = prev1 + prev0
        prev0 = prev1
        prev1 = temp
    return prev1
print(fibonacci(8))