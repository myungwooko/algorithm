"""
1099. Two Sum Less Than K
Easy

Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i,
j exist satisfying this equation, return -1.

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation:
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation:
In this case it's not possible to get a pair sum less that 15.


Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""


class Solution:
    def twoSumLessThanK(self, A, K):
        A.sort()
        l, r, res = 0, len(A) - 1, -1
        while l < r:
            if A[l] + A[r] >= K:
                r -= 1
            else:
                res = max(res, A[l] + A[r])
                l += 1
        return res

    # def twoSumLessThanK(self, A, K):
    #     self.K = K
    #     dic = {}
    #     for i in range(len(A)):
    #         dic[i] = self.trimArr(A, i)
    #     values = dic.values()
    #     res = [e for s in values for e in s]
    #     if not res:
    #         return -1
    #     return max(res)
    #
    # def trimArr(self, arr, i):
    #     val = arr[i]
    #     arr = arr[:i] + arr[i+1:]
    #     arr = [e + val for e in arr if e + val < self.K]
    #     return arr


A, K = [34, 23, 1, 24, 75, 33, 54, 8], 60
s = Solution()
test = s.twoSumLessThanK(A, K)
print(test)
