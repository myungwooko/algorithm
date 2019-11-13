"""
48. Rotate Image
Medium

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

mySolution
        -
        00 01 02 03      03 13 23 33
        10 11 12 13      02 12 22 32
        20 21 22 23      01 11 21 31
        30 31 32 33      00 10 20 30
        -
        max = len-1(=3), min = 0

           position  direction
        -> up        right    : fix x(max) / y asc(min->max)
        |y right     down     : des x(max->min) / fix y(max)
        <- down      left     : fix x(min) / y dec(max->min)
        ^| left      up       : asc x(min->max) / fix y(min)
        -
        next
        min -> +1
        max -> -1
        -
        if max > min => do same position and direction thing.

        **********************************************************************
        BUT ******************************************************************
        => WHEN YOU LOOK AT THE CHANGED ONE => YOU CAN FIND OUT SIMPLE PATTERN
        => Y ASC, X FIX => X -= 1 => Y ASC, X FIX => GO ON
        **********************************************************************
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        fixedX = n - 1

        preRes = []
        for _ in range(n):
            row = [0]*(n)
            preRes.append(row)
        for y in range(n):
            for x in range(n):
                preRes[x][fixedX] = matrix[y][x]
            fixedX -= 1
        for y in range(n):
            for x in range(n):
                matrix[y][x] = preRes[y][x]

        print(matrix)
        return

        # 00 01 02 03      03 13 23 33
        # 10 11 12 13      02 12 22 32
        # 20 21 22 23      01 11 21 31
        # 30 31 32 33      00 10 20 30
    def rotate2(self, matrix):
        n = len(matrix)
        for l in range(n / 2):
            r = n - 1 - l
            for p in range(l, r):
                q = n - 1 - p
                cache = matrix[l][p]
                matrix[l][p] = matrix[q][l]
                matrix[q][l] = matrix[r][q]
                matrix[r][q] = matrix[p][r]
                matrix[p][r] = cache

inputM =[
     [1,2,3],
     [4,5,6],
     [7,8,9]
    ]

s = Solution()
test = s.rotate(inputM)




















