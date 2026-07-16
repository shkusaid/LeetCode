# __________________________ BRUTE FORCE SOLUTION _______________________

# def collision(aestroids):
#     if len(aestroids) < 2:
#         return aestroids
#     i = 0
#     while i < len(aestroids) -1:
#         if aestroids[i] > 0 and aestroids[i+1] < 0:
#             if aestroids[i] > -aestroids[i+1]:
#                 aestroids.pop(i+1)
#             elif aestroids[i] < -aestroids[i+1]:
#                 aestroids.pop(i)
#                 if i > 0:
#                     i -= 1
#             else:
#                 aestroids.pop(i + 1)
#                 aestroids.pop(i)
#                 if i > 0:
#                     i -= 1
#         else:
#             i += 1
#     return aestroids

# ________________________ OPTIMAL SOLUTION _____________________

def collision(aestroids):
    Stack = []
    for aestroid in aestroids:
        while Stack and Stack[-1] > 0 and aestroid < 0 and Stack[-1] < -aestroid:
            Stack.pop()
        if Stack and aestroid < 0 and Stack[-1] > 0:
            if -aestroid == Stack[-1]:
                Stack.pop()
        else:
            Stack.append(aestroid)
    return Stack
        
print(collision([5, 10, -5]))       # [5, 10]
print(collision([8, -8]))           # []
print(collision([10, 2, -5]))       # [10]
print(collision([-2, -1, 1, 2]))    # [-2, -1, 1, 2]
print(collision([1, 2, 3, -5]))     # [-5]
print(collision([5, 10, -5, -10]))  # [5]