# def basic_cal(s):
#     nums = []
#     ops = []
#     num = 0
#     for ch in s:
#         if ch == " ":
#             continue
#         if ch.isdigit():
#             num = num * 10 + int(ch)
#         else:
#             nums.append(num)
#             ops.append(ch)
#             num = 0
#     nums.append(num)
#     i = 0
#     while i < len(ops):
#         if ops[i] == "*":
#             nums[i] *= nums[i + 1]
#             nums.pop(i + 1)
#             ops.pop(i)
#         elif ops[i] == "/":
#             nums[i] //= nums[i + 1]
#             nums.pop(i + 1)
#             ops.pop(i)
#         else:
#             i += 1
#     result = nums[0]
#     for i in range(len(ops)):
#         if ops[i] == "+":
#             result += nums[i + 1]
#         else:
#             result -= nums[i+ 1]
#     return result

def basic_cal(s):
    Stack = []
    op = "+" 
    num = 0
    for i in range(len(s) + 1):
        ch = "+" if i == len(s) else s[i]
        if ch == " ":
            continue
        if ch.isdigit():
            num = num * 10 + int(ch)
        else:
            if op == "+":
                Stack.append(num)
            elif op == "-":
                Stack.append(-num)
            elif op == "*":
                Stack.append(Stack.pop() * num)
            else:
                Stack.append(int(Stack.pop() / num))
            op = ch
            num = 0
    return sum(Stack)

s = " 3/2 "
print(basic_cal(s))