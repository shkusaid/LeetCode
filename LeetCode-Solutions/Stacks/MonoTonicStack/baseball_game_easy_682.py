def baseball_game(nums):
    Stack = []
    for num in nums:
        if num.lstrip("-").isdigit():
            Stack.append(int(num))
        elif num == "C" and len(Stack) >= 1:
            Stack.pop()
        elif num == "D" and len(Stack) >= 1:
            Stack.append(2 * Stack[-1])
        elif num == "+" and len(Stack) >= 2:
            Stack.append(Stack[-1] + Stack[-2])
    return sum(Stack)

ops = ["5","-2","4","C","D","9","+","+"]
print(baseball_game(ops))