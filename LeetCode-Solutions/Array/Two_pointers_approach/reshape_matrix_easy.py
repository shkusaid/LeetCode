def reshape(mat , c , r):
    m , n = len(mat) , len(mat[0])
    if m * n != c * r:
        return mat
    x = y = 0
    ans = [[0] * c for _ in range(r)]
    for i in range(m):
        for j in range(n):
            ans[x][y] = mat[i][j]
            y += 1
            if y == c:
                 y = 0
                 x += 1
    return ans

mat = [[1 , 2] , [3 , 4]]
c , r = 4 , 1
print(reshape(mat , c , r))