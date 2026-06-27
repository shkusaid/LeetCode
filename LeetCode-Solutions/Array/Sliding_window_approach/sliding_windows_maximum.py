# def sliding_window_max(arr , k):
# _______________________________ BRUTE FORCE APPROACH _________________________
    # result = [0] * (len(arr) - k + 1)
    # for i in range(len(arr) - k + 1):
    #     maximum = arr[i]        
    #     for j in range(i , i + k):
    #         maximum = max(maximum , arr[j])
    #     result[i] = maximum
    # return result
# ________________________________ OPTIMAL APPROACH __________________________

from collections import deque
def sliding_window_max(arr , k):
    n = len(arr)
    result = [0] * (n - k + 1)
    que = deque()
    for right in range(n):
        while que and que[0] <= right - k:
            que.popleft()
        while que and arr[que[-1]] < arr[right]:
            que.pop()
        que.append(right)
        if right >= k - 1:
            result[right - k + 1] = arr[que[0]]
    return result
arr = [1,3,-1,-3,5,3,6,7]
print(sliding_window_max(arr , 3))