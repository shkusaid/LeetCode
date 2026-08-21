def max_wealth(arr):
    max_money = 0
    for i in range(len(arr)):
        max_money = max(max_money , sum(arr[i]))
    return max_money

arr = [[1 , 2, 3] , [4 , 5, 6] , [7 , 8 , 9]]
print(max_wealth(arr))