"""
74. Search a 2D Matrix
Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        theRow = []
        for row in matrix:
            if row[0] <= target and target <= row[-1]:
                theRow = row
                break

        if not theRow:
            return False

        l, r = 0, len(theRow) - 1
        while l < r:
            mid = (l + r) // 2
            if theRow[mid] < target:
                l = mid + 1
            else:
                r = mid
        if theRow[l] == target:
            return True

        return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
s = Solution()
test = s.searchMatrix(matrix, 0)
print(test)





