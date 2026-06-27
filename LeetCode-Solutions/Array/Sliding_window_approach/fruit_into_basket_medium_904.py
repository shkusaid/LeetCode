# ___________________________ BRUTE FORCE APPROACH T.C O(n ^ 2) __________________________
# def fruits_into_basket(fruits):
#     n = len(fruits)
#     max_fruit = 0
#     for l in range(n):
#         frequency = {}
#         for r in range(l , n):
#             frequency[fruits[r]] = frequency.get(fruits[r],0) + 1
#             if len(frequency) > 2:
#                 break
#             max_fruit = max(max_fruit , r - l + 1)
#     return max_fruit

# print(fruits_into_basket([2, 1, 2, 1, 3, 3]))

# ____________________________ OPTIMAL APPROACH T.C O(n) _________________________________

def fruits_into_basket(fruits):
    n = len(fruits)
    left = 0
    max_count = 0
    fruits_map = {}
    for right in range(n):
        fruits_map[fruits[right]] = fruits_map.get(fruits[right] , 0) + 1
        while len(fruits_map) > 2:
            fruits_map[fruits[left]] -= 1
            if fruits_map[fruits[left]] == 0:
                del fruits_map[fruits[left]]
            left += 1
        max_count = max(max_count, right - left + 1)
    return max_count

print(fruits_into_basket([2, 1, 2, 1, 3, 3]))