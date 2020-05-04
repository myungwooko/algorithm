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


# Time Complexity and Space complexity => O(m*n) <= recursion is not that simply clear
# Because of the deletion is too expensive
# improved by using seen
def spiral_copy(matrix):
    if not matrix:
        return []
    seen = set()
    count = 0
    result = []

    def helper(direction, r, c, result, count):
        if count == len(matrix) * len(matrix[0]):
            return
        if direction == "right":
            while c < len(matrix[0]) and (r, c) not in seen:
                result.append(matrix[r][c])
                count += 1
                seen.add((r, c))
                c += 1
            c -= 1
            helper("down", r + 1, c, result, count)
        elif direction == "down":
            while r < len(matrix) and (r, c) not in seen:
                result.append(matrix[r][c])
                count += 1
                seen.add((r, c))
                r += 1
            r -= 1
            helper("left", r, c - 1, result, count)
        elif direction == "left":
            while c >= 0 and (r, c) not in seen:
                result.append(matrix[r][c])
                count += 1
                seen.add((r, c))
                c -= 1
            c += 1
            helper("up", r - 1, c, result, count)
        elif direction == "up":
            while r >= 0 and (r, c) not in seen:
                result.append(matrix[r][c])
                count += 1
                seen.add((r, c))
                r -= 1
            r += 1
            helper("right", r, c + 1, result, count)

    helper("right", 0, 0, result, count)
    return result


# Way better
# Time Complexity and Space complexity => O(m*n)
def spiral_copy(matrix):
    if not matrix:
        return []
    result = []
    topRow = 0
    btmRow = len(matrix) - 1
    leftCol = 0
    rightCol = len(matrix[0]) - 1
    while len(result) < len(matrix) * len(matrix[0]):
        # while topRow <= btmRow and leftCol <= rightCol:
        for i in range(leftCol, rightCol + 1):
            result.append(matrix[topRow][i])
        topRow += 1

        for j in range(topRow, btmRow + 1):
            result.append(matrix[j][rightCol])
        rightCol -= 1

        """ 
        This is the key
        지나갔다는것은 같은 해당 btmRow에 대해서 이미 했다는게 되므로 그것은 중복, 그러므로 해당 check 필요.
        """
        if topRow <= btmRow:
            for k in range(rightCol, leftCol - 1, -1):
                result.append(matrix[btmRow][k])
            btmRow -= 1

        """as same as that one"""
        if leftCol <= rightCol:
            for l in range(btmRow, topRow - 1, -1):
                result.append(matrix[l][leftCol])
            leftCol += 1

    return result


input = [[6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]]
test = spiral_copy(input)
print(test)