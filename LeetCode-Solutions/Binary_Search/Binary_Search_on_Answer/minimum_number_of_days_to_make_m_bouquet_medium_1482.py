def minimum_number_of_days(bloomdays , m , k):
    if len(bloomdays) < m * k:
        return -1
    def can_make(bloomdays , m ,k , days):
        count = b =0
        for i in range(len(bloomdays)):
            if bloomdays[i] <= days:
                count += 1
                if count == k:
                    b += 1
                    count = 0
            else:
                count = 0
        return b >= m
    low = min(bloomdays)
    high = max(bloomdays)
    ans = -1
    while low <= high:
        mid = low + (high - low ) // 2
        if can_make(bloomdays , m , k , mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

bloomdays = [ 1, 10 , 3, 10 , 2]
print(minimum_number_of_days(bloomdays , 3 , 1))