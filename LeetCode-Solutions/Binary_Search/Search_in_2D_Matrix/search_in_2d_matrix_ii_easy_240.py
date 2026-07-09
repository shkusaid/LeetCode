def search_in_2d_matrix(matrix , target):
    rows = len(matrix)
    r = 0
    c = len(matrix[0]) - 1
    while r < rows and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1
        else:
            r += 1
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 0

print(search_in_2d_matrix(matrix , target))