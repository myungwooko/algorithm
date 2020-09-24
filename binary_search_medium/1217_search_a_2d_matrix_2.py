"""
240. Search a 2D Matrix II
Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 1. 0 row에서 큰것들은 일단 날려 x의 range를 정한다.
        # 2. 마지막 row에서 해당 range의 index중 target보다 작은것들은 날린다.
        # 범위가 정해진다.
        # 각각의 column에 대해서 binary search를 사용하여 target을 찾는다.
        if not matrix or not matrix[0] or target is None:
            return False
        r = len(matrix[0]) - 1
        while r > 0 and target < matrix[0][r]:
            r -= 1
        if r < 0:
            return False
        l = 0
        while l < len(matrix[-1]) and target > matrix[-1][l]:
            l += 1
        if l >= len(matrix[-1]):
            return False
        if l > r:
            return False
        res = []
        for i in range(l, r + 1):
            res.append(self.helper(i, matrix, target))
        res = set(res)
        if True in res:
            return True
        return False

    def helper(self, c, matrix, target):
        u, d = 0, len(matrix) - 1
        while u <= d:
            if u == d:
                return matrix[u][c] == target
            mid = u + (d - u) // 2
            midVal = matrix[mid][c]
            if midVal == target:
                return True
            elif midVal > target:
                d = mid - 1
            else:
                u = mid + 1
        return False

    """
    Starting with the bottom left corner of the matrix, if the current element curr equals target, we return True. 
    If curr is larger than target, than since any element to the right of curr (in the same row) is larger than curr, 
    we don't need to consider them, so we deduct the row index by 1 (move up by 1 row). By the same token, 
    if curr is smaller than target, we increase the column index by 1 (move right by 1 column). Repeat the above steps 
    until we find target in which case we return True or move out of matrix in which case we return False.
    Time complexity: O(m+n), space complexity: O(1).
    """

    def searchMatrix2(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        y = m - 1
        x = 0
        while x < n and y >= 0:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                x += 1
            else:
                y -= 1
        return False

    #O(n)
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)


matrix = [[-5]]
target = -2
s = Solution()
test = s.searchMatrix(matrix, target)
print(test)
