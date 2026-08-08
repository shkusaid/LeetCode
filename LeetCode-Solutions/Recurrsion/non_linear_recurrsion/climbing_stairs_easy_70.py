# ______________________ S.C is 0(n)
# def climbing_stairs(n):
#     arr = [1 , 2]
#     for i in range(3 , n + 1):
#         arr.append(arr[i-1] + arr[i - 2])
#     return arr[n]
# print(climbing_stairs(8))

# _______________________ T.C is 2 ^ n _____________________
# def climbing_stairs(n):
#     if n == 1 or n == 2:
#         return n
#     return climbing_stairs(n - 1) + climbing_stairs(n - 2)
# print(climbing_stairs(8))

# _______________________ Linear T.C and S.C ______________________
def climbing_stairs(n):
    if n==1 or n==2:
        return n
    prev0 = 0
    prev1 = 1
    for i in range(3 , n + 1):
        temp = prev1 + prev0
        prev0 = prev1
        prev1 = temp
    return prev1
print(climbing_stairs(8))