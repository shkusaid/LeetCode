def remove_zero_and_multiply_sum(x):
    place = 1
    number = 0
    sum = 0
    while x > 0:
        digit = x % 10
        if digit != 0:
            sum += digit
            number = number + (digit * place)
            place *= 10
        x //= 10
    return number * sum
    

x = 1020304 # ans will be 1234
print(remove_zero_and_multiply_sum(x))