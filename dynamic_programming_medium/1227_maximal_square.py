"""
221. Maximal Square
Medium

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) < 1:
            return 0
        maxS = [0]
        maxR = len(matrix) - 1
        maxC = len(matrix[0]) - 1

        def squareChecker(r, c):
            count = 0
            print(33, 'r, c', r, c, count)
            if matrix[r][c] == "1":
                count += 1
            startR = r
            startC = c
            while r + 1 <= maxR and c + 1 <= maxC:
                r += 1
                c += 1
                print(r, c)
                if matrix[r][c] == "1":
                    checker = True
                    for rr in range(startR, r):
                        if matrix[rr][c] != "1":
                            checker = False
                            break
                    if not checker:
                        break
                    for cc in range(startC, c):
                        if matrix[r][cc] != "1":
                            checker = False
                            break
                    if not checker:
                        break
                    count += 1
                else:
                    break
            print('count', count)
            if count > maxS[0]:
                maxS[0] = count

        for r in range(len(matrix)):
            if maxR - r < maxS[0]:
                continue
            for c in range(len(matrix[0])):
                if maxC - c < maxS[0]:
                    continue
                print(65, r, c)
                squareChecker(r, c)
        return pow(maxS[0], 2)

    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        r, c = len(matrix), len(matrix[0])
        pre = cur = [0] * (c + 1)
        res = 0
        print(pre, cur)
        for i in range(r):
            for j in range(c):
                cur[j + 1] = (min(pre[j], pre[j + 1], cur[j]) + 1) * int(
                    matrix[i][j])
                res = max(res, cur[j + 1]**2)
                print(cur, pre)
            pre = cur
            cur = [0] * (c + 1)
        return res

    """
    본인이 일단 기본적으로 1인 경우
    본인의 왼쪽, 본인의 좌측 상단 대각선, 본인의 위쪽 요 세개중에 min을 구해 +1을 자기자신으로 하는 식으로 dp를 해나가면 된다. 
    그렇게 만들어져있는 세개의 수가 자신이 포함되어있는 최대 사각형의 크기의 제곱근으로 되는 구조. 그림을 그려보면 그 제곱근이 1로 이루어지는 사각형의 한변의 길이가 되고 
    해당 수들이 그렇게 자신의 사각형을 나타내고 있다면 그렇게 될 수 밖에 없는 구조.
    예술이다 ㅜㅜ 
    It's kind of art
    """

    def maximalSquare(self, matrix):
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(n)]
              for i in range(m)]
        print(1, dp)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                   dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0
        print(1, dp)
        ans = max([max(i) for i in dp])
        return ans**2


matrix = [["1", "1", "1", "1", "1", "1"], ["0", "1", "1", "1", "1", "1"],
          ["1", "1", "1", "1", "0", "1"], ["1", "1", "1", "1", "1", "1"]]
s = Solution()
test = s.maximalSquare(matrix)
print(test)
"""
[
 [1, 1, 1, 1, 1, 1],
 [0, 1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 0, 1], 
 [1, 1, 1, 1, 1, 1]
]
 
[
[1, 1, 1, 1, 1, 1], 
[0, 1, 2, 2, 2, 2], 
[1, 1, 2, 3, 0, 1], 
[1, 2, 2, 3, 1, 1]
]
"""
