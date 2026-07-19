def basic_cal(s):
    Stack = []
    num = result = 0
    sign = 1
    for ch in s:
        if ch == " ":
            continue
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "+":
            result += sign * num
            num = 0
            sign = 1
        elif ch == "-":
            result += sign * num
            num = 0
            sign = -1
        elif ch == "(":
            Stack.append(result)
            Stack.append(sign)
            result = 0
            sign = 1
        elif ch == ")":
            result += sign * num
            num = 0
            result *= Stack.pop() # For sign before "("
            result += Stack.pop() # for result before "("
    return result + sign * num

s = "(1+(4+5+2)-3)+(6+8)"
print(basic_cal(s))