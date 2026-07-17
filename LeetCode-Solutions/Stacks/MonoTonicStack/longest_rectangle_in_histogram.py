# def longest_rectangle(hist):
#     n = len(hist)
#     max_ans = 0
#     for i in range(n):
#         height = hist[i]
#         for j in range(i,n):
#             height = min(height , hist[j])
#             width = j - i + 1
#             ans = height * width
#             max_ans = max(max_ans , ans)
#     return max_ans

def longest_rectangle(heights):
    n = len(heights)
    Stack = []
    max_area = 0
    for i in range(n + 1):
        h = 0 if i == n else heights[i]
        while Stack and heights[Stack[-1]] > h:
            height = heights[Stack.pop()]
            width = i if not Stack else i - Stack[-1] - 1
            area = height * width
            max_area = max(max_area , area)
        Stack.append(i)
    return max_area
heights = [2, 1, 5, 6, 2, 3]
print(longest_rectangle(heights))