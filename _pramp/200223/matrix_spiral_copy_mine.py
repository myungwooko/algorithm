"""
Matrix Spiral Copy
Given a 2D array (matrix) inputMatrix of integers, create a function spiralCopy that copies inputMatrix’s values into a
1D array in a spiral order, clockwise. Your function then should return that array. Analyze the time and space complexities of your solution.

Example:
input:  inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
See the illustration below to understand better what a clockwise spiral order looks like.

altClockwise spiral order

Constraints:
- [time limit] 5000ms
- [input] array.array.integer inputMatrix

1 ≤ inputMatrix[0].length ≤ 100
1 ≤ inputMatrix.length ≤ 100
[output] array.integer
"""
"""
Just using direction and each direction has their own logic

input:  inputMatrix  = 
[
 [6,    7,   8,  9,   10],
 [11,  12,  13,  14,  15],
 [16,  17,  18,  19,  20] 
]

right => down => left => up
[1,2,3,4,5,10,15,20,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12]
"""
# Time complexit mxn => O(mn)? => No
# => Because delete Item time complexity     => O(n)
# => Because pop intermediat item of index k => O(k)
# It's time complexity greater than O(mn)
def spiral_copy(inputMatrix):
    if not inputMatrix:
        return []
    original = inputMatrix[:]
    result = []

    def helper(matrix, direction, result):
        if matrix and direction == "right":
            result += matrix[0]
            matrix.pop(0)
            helper(matrix, "down", result)
        elif matrix and direction == "down":
            last_col = len(matrix[0]) - 1
            for i in range(len(matrix)):
                result.append(matrix[i].pop())
            helper(matrix, "left", result)
        elif matrix and direction == "left":
            last_row = matrix.pop()
            reverse = last_row[::-1]
            result += reverse
            helper(matrix, "up", result)
        elif matrix and direction == "up":
            for i in range(len(matrix) - 1, -1, -1):
                result.append(matrix[i].pop(0))
            helper(matrix, "right", result)

    helper(inputMatrix, "right", result)
    return result

