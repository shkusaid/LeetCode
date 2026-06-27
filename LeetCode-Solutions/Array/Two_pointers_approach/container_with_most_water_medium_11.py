def water(height):
    i = 0
    j = len(height) - 1
    max_sum = 0
    while i < j:
        h = min(height[i] , height[j])
        w = j - i
        area = h * w
        if height[i] < height[j]:
            i+=1 
        else:
            j-=1
        max_sum = max(max_sum, area)
    return max_sum

h = [1, 8, 6, 2, 5, 4, 8, 7]
print(water(h))
            