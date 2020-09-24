"""
54. Spiral Matrix
Medium

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:              y = 3, x = 3
[
 [ 1, 2, 3 ],       00 01 02 -> 12 22  -> 21 20  -> 10 11
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:               y = 3, x = 4
[
  [1, 2, 3, 4],      00 01 02 03  -> 13 23 -> 22 21 20 -> 10 11 12
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Using recursion makes it really easy!!!!!!!!

- 방향은 1, 2, 3
1 => 맨위에만 오른쪽으로 가면서 넣고 해당 부분자르고 다음 방향이랑 넣기
2 => 맨오른쪽만 아래쪽으로 가면서 넣고 해당 부분자르고 다음 방향이랑 넣기
3 => 맨아래만 왼쪽으로 가면서 넣고 해당 부분 자르고 넣기
4 => 맨왼쪽만 위로 가면서 넣고 해당 부분 자르고 넣기
- 자르고 나머지 넣고 방향만 주면
- ok
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        res = []
        total = len(matrix) * len(matrix[0])
        self.helper(matrix, 1, res, total)
        return res

    def helper(self, matrix, direction, res, total):
        if len(res) == total:
            return res

        if direction == 1:
            theLine = matrix[0]
            for i in theLine:
                res.append(i)
            del matrix[0]
            self.helper(matrix, 2, res, total)

        if direction == 2:
            for i, row in enumerate(matrix):
                res.append(row[-1])
                matrix[i] = matrix[i][:-1]
            self.helper(matrix, 3, res, total)

        if direction == 3:
            theLine = matrix[-1]
            theLine.reverse()
            for i in theLine:
                res.append(i)
            del matrix[-1]
            self.helper(matrix, 4, res, total)

        if direction == 4:
            for i in reversed(range(len(matrix))):
                res.append(matrix[i][0])
                matrix[i] = matrix[i][1:]
            self.helper(matrix, 1, res, total)


s = Solution()
input = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
test = s.spiralOrder(input)
print('result: ', test)
