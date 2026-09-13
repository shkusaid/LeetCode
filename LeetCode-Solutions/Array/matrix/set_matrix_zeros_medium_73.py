def set_matrix_zeros(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row = [False] * m
    col = [False] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
    for i in range(m):
        for j in range(n):
            if row[i] or col[j]:
                matrix[i][j] = 0
    return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(set_matrix_zeros(matrix))