"""
264. Ugly Number II
Medium

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
"""


class Solution(object):
    # time limit exceeded
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0 or n > 1690:
            return
        dp = [1, 2, 3, 4, 5]
        if n <= 5:
            return dp[n - 1]

        falseCount = 0
        num = 6
        while len(dp) - falseCount < n:
            q, r = divmod(num, 2)
            if r == 0 and dp[q - 1]:
                dp.append(num)
                num += 1
                continue
            q, r = divmod(num, 3)
            if r == 0 and dp[q - 1]:
                dp.append(num)
                num += 1
                continue
            q, r = divmod(num, 5)
            if r == 0 and dp[q - 1]:
                dp.append(num)
                num += 1
                continue
            dp.append(False)
            falseCount += 1
            num += 1

        for i in range(len(dp) - 1, -1, -1):
            if dp[i]:
                return dp[i]

    # 제일 작은 수일때 자신만큼의 수를 더하는 식의 곱하는 수 1이증가
    # 1이 들어있기 때문에 처음 ugly[i2, i3, i4] => ugly[0]은 모두 1을 가리킴
    # index로 ugly에 순차적으로 접근해서 각각 자신을 곱하고 작은 순으로 append.
    # 제일 작았을때 넣고 인덱스값 1 증가 시켜 나감.
    # 결국 2의 배수, 3의 배수, 5의 배수로 나아가고 자신들 사이에서 만들어진 ugly수들의 증가하는 것에 자신들을 한번씩 또 곱해나가면 수를 만들어나가는것.
    # 즉, 2, 3, 5로 이루어진 product만 나올수 밖에 없게 하는 것이며 모든 수들을 다 거치게 된다.
    def nthUglyNumber(self, n):
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            print(umin)
            ugly.append(umin)
            n -= 1
        print(ugly)
        return ugly[-1]


s = Solution()
test = s.nthUglyNumber(15)
print(test)
