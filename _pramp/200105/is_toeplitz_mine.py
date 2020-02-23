"""
Toeplitz Matrix
A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element. Given a non-empty matrix arr,
write a function that returns true if and only if it is a Toeplitz matrix. The matrix can be any dimensions, not necessarily square.

For example,

[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]

is a Toeplitz matrix, so we should return true, while

[[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]

isn’t a Toeplitz matrix, so we should return false.

Constraints:

[time limit] 5000ms
[input] array.array.integer arr
0 ≤ arr.length ≤ 20
0 ≤ arr[i].length ≤ 20
0 ≤ arr[i][j] ≤ 20
[output] boolean
"""
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

def isToeplitz(matrix):
    if not matrix or not matrix[0]:
        return False
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True


arr = [[1, 2, 3, 4],
       [5, 1, 2, 3],
       [6, 5, 1, 2]]

print(isToeplitz(arr))