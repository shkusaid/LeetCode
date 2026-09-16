def two_city_schedule(costs):
    n = len(costs)
    for i in range(n):
        for j in range(i + 1, n):
            if costs[i][0] - costs[i][1] > costs[j][0] - costs[j][1]:
                costs[i] , costs[j] = costs[j] , costs[i]
    total = 0
    for i in range(n):
        if i < n // 2:
            total += costs[i][0]
        else:
            total += costs[i][1]
    return total

costs = [[10,20],[30,200],[400,50],[30,20]]
print(two_city_schedule(costs))