# _____________________ BRUTE FORCE APPROACH _______________

# import math
# def min_speed(dist , hours):
#     def distance(dist , speed):
#         time = 0
#         for j in range(len(dist)):
#             t = dist[j] / speed
#             if j != len(dist) - 1:
#                 time += math.ceil(t)
#             else:
#                 time += t
#         return time
#     low = 1
#     high = 10 ** 7
#     ans = 0
#     for speed in range(low , high + 1):
#         if distance(dist, speed) <= hours:
#             return speed
#     return -1

# _________________________OPTIMAL APPROACH __________________
import math
def min_speed(dist , hours):
    def can_reach(dist , hours , speed):
        time = 0
        for j in range(len(dist)):
            t = dist[j] / speed
            if j == len(dist) - 1:
                time += t
            else:
                time += math.ceil(t)
        return time <= hours
    low = 1
    high = 10 ** 7
    ans = -1
    while low <= high:
        speed = low + (high - low) // 2
        if can_reach(dist , hours , speed):
            ans = speed
            high = speed - 1
        else:
            low = speed + 1
    return  ans

dist = [1 , 3, 2]
print(min_speed(dist , 6))