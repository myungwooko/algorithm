"""
119. Pascal's Triangle II
Easy

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
"""
class Solution:
    def getRow(self, rowIndex: int):
        pascal = [[1]*(i+1) for i in range(rowIndex)]

        for i in range(pascal):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

        return pascal[-1]
