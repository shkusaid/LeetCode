def sqrt(x):
    if x < 2:
        return x
    left = 0
    right = x//2
    while left <= right:
        mid = left + ((right - left) // 2)
        square = mid * mid
        if square == x:
            return mid
        elif square > x:
            right = mid - 1
        else:
            left = mid + 1
    return right # bcz right cross left and we've to return floor value means sqrt of 8 is 2.82
                    # we've to return 2

print(sqrt(100))