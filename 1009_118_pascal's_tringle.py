"""
118. Pascal's Triangle
Easy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows: int):
        if not numRows:
            return []
        elif numRows == 1:
            return [[1]]

        result = [[1], [1,1]]
        current = [1]
        count = numRows - 2

        while count:
            last = result[-1]
            for i, v in enumerate(last):
                if i < len(last) - 1:
                    added = v + last[i+1]
                    current.append(added)

            current.append(1)
            result.append(current)
            current = [1]
            count -= 1

        return result

    def generate1(self, numRows):
        pascal = [[1] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal


s = Solution()
test = s.generate(5)
print(test)