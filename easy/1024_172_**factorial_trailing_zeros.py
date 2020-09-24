"""
172. Factorial Trailing Zeroes
Easy

Share
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

We add a trailing zero every time we multiply by 10 (5 * 2). Since we will have always more 2s than 5s, ***5만큼 커지면 2만큼은 두번 커지니까
the problem is to find the number of 5s in the numbers from 1 to n.
Let's consider 10! as example:

10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

In this case, we have two 5s (in 10 and 5), so the result is 2. How can we efficiently compute this number for a given n?
Well, we could compute the multiple of 5 contained in n, but this is not enough: for example, 25 accounts for 2 5s, 50 accounts also for 2 5s, and so on.
5가 여러개 있는 경우 그 여러번을 모두 카운트해준다. 5의 배수중 중복가능성을 고려해 체크해주는 수는 최대 n(인자로 들어온) 자신을 최대로 한다.
* 두번째 돌면서는 두번 들어간거 체크, 세번째 돌면서는 세번 들어간거 체크...

So, we do the following: we start from 5, and we see how many multiples of 5 we have in n. Then, we multiply 5 by 5 (25)
and we add how many multiples of 25 we have in n. In this case we will not have duplicates, as at in each step we will add only one 5 to the result.
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        d, count = 5, 0
        while d <= n:
            count += n // d
            d *= 5
        return count

    def trailingZeroes2(self, n):
        k, tot = 5, 0
        while k <= n:
            tot += n // k
            k = k * 5
        return tot


s = Solution()
test = s.trailingZeroes(50)

print(1, test)
