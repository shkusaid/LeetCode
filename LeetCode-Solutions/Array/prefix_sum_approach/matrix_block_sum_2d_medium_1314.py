#  ____________________________ BRUTE FORCE APPROACH __________________________

# def matrix_sum(mat , k):
#     m = len(mat)
#     n = len(mat[0])
#     answer = [[0] * n for _ in range(m)]
#     for i in range(m):
#         for j in range(n):
#             value = 0
#             for r in range(i-k , i+k+1):
#                 for c in range(j-k , j+k+1):
#                     if r >= 0 and r < m and c >= 0 and c < n:
#                         value += mat[r][c]
#             answer[i][j] = value
#     return answer



# ______________________________ OPTIMAL APPROACH _____________________________ 

def matrix_sum(mat , k):
    m = len(mat)
    n = len(mat[0])
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1 ,m+1):
        for j in range(1 , n+1):
            prefix[i][j] = mat[i -1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
    answer = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            r1 = max(0 , i - k)
            c1 = max(0 , j - k)
            r2 = min(m - 1, i + k)
            c2 = min(n - 1, j + k)
            r1 += 1
            c1 += 1
            r2 += 1
            c2 += 1
            answer[i][j] = prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1]
    return answer
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix_sum(mat , 1))