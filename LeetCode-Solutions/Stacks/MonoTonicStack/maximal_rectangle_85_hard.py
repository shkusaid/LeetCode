def maximal_rectangle(matrix):
    def is_all_ones(matrix , row1 , col1 , row2, col2):
        for i in range(row1 , row2 + 1):
            for j in range(col1 , col2 + 1):
                if matrix[i][j] == "0":
                    return False
        return True
    
    rows = len(matrix)
    cols = len(matrix[0])
    max_area = 0
    for r1 in range(rows):
        for c1 in range(cols):
            if matrix[r1][c1] == "0":
                continue
            for r2 in range(r1 , rows):
                for c2 in range(c1 , cols):
                    if is_all_ones(matrix , r1 , c1 , r2 , c2):
                        area = (r2 - r1 + 1) * (c2 - c1 + 1)
                        max_area = max(max_area , area)
    return max_area

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximal_rectangle(matrix))