"""
279. Perfect Squares
Medium

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
from math import sqrt
import collections


# 해당 연산때마다 1을 더해주는 이유는 제곱근은 뺴주며 총 합에서 제외 시켰으므로 그 완전제곱수의 연산에 사용된 숫자에 대한 카운트를 해주는 것.
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # it says it is for only positive integers.
        if n == 1:
            return 1
        if n < 1:
            return

        def helper(dp, n):
            if n <= 1:
                return n
            elif n in dp:
                return dp[n]
            else:
                dp[n] = float("inf")
                s = int(sqrt(n))
                # 만드는 과정에서 가능한 완전제곱수들을 경우별로 뺐을때
                # 각각의 나머지 수들이 또 다른 완전제곱수 일수도 있고 아닐수도 있는데 크기와 상관없이 그것을 만드는 개수는 그변칙적이므로 모든 경우들을 체크해줘야 한다.
                for i in range(s, 0, -1):
                    dp[n] = min(dp[n], helper(dp, n - i * i) + 1)
                return dp[n]

        return helper({}, n)


n = 15
s = Solution()
test = s.numSquares(n)
print(test)

li = []
for i in range(100):
    li.append(s.numSquares(i))
print(li)
