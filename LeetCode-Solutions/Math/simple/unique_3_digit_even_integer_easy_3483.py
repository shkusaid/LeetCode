def three_digit_even_integer(digits):
    nums = set()
    n = len(digits)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or j == k or i == k:
                    continue
                if digits[i] == 0 or digits[k] % 2 != 0:
                    continue
                num = digits[i] * 100 + digits[j] * 10 + digits[k]
                nums.add(num)
    return len(nums)

digits = [2 , 1, 3, 0]
print(three_digit_even_integer(digits))