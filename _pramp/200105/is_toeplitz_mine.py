def isToeplitz(arr):
    maxRow = len(arr)
    maxCol = len(arr[0])

    def nextChecker(r, c):
        if (r + 1 == maxRow or c + 1 == maxCol):
            return True
        if arr[r][c] == arr[r + 1][c + 1]:
            return nextChecker(r + 1, c + 1)
        else:
            return False

    for c in range(len(arr[0]) - 1):
        if not nextChecker(0, c):
            return False

    for r in range(len(arr) - 1):
        if not nextChecker(r, 0):
            return False
    return True


arr = [[1, 2, 3, 4],
       [5, 1, 2, 3],
       [6, 3, 1, 2]]

print(isToeplitz(arr))