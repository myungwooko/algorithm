def print_diagonals(matrix):
    m = len(matrix)
    n = len(matrix[0])

    def print_diagonal(r, c):
        # print diagonal from coordinate
        res = []
        while c >= 0 and r < m:
            res.append(matrix[r][c])
            r += 1
            c -= 1
        print(res)

    for c in range(n - 1):
        print_diagonal(0, c)

    for r in range(m):
        print_diagonal(r, n - 1)
    return


matrix = [[9, 3, 2],
          [8, 6, 1],
          [5, 5, 6],
          [1, 2, 8]]

print(print_diagonals(matrix))

# 9
# 3 8
# 2 6 5
# 1 5 1
# 6 2
# 8
