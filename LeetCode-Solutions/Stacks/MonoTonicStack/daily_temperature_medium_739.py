# _____________________ BRUTE FORCE APPROACH _________________________

# def daily_temperature(temp):
#     n = len(temp)
#     ans = [0] * n
#     for i in range(n - 1):
#         for j in range(i+ 1 , n):
#             if temp[j] > temp[i]:
#                 ans[i] = j - i
#                 break
#     return ans


# ______________________ OPTIMAL APPROACH ____________________

def daily_temperature(temp) :
    n = len(temp)
    Stack = []
    answer = [0] * n
    for i in range(n-1 , -1 , -1):
        while Stack and temp[Stack[-1]] <= temp[i]:
            Stack.pop()
        if Stack:
            answer[i] = Stack[-1] - i
        Stack.append(i)
    return answer
temp = [73,74,75,71,69,72,76,73]
print(daily_temperature(temp))