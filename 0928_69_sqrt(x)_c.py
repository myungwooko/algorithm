"""
69. Sqrt(x)
Easy

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # implement math.sqrt()
        # @ only positive integer
        # @ return the squre root
        # @ truncate to only integer
        # if put 0 => return 0
        # pow(int1) == x ==> return int1
        # pow(int1) < x , x < pow(int2) ==> return int1
        # left right => O(lonN)

        count = 0
        half = x // 2
        while True:
            count+=1
            if half * half <= x < (half + 1) * (half + 1):
                return count, half
            elif half * half > x:
                half = half // 2
            elif half * half < x:
                half += 1

    # def mySqrt2(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     count = 0
    #     left, right = 1, x
    #     while left <= right:
    #         count+=1
    #         mid = (left + right) // 2
    #         if mid**2 == x:
    #             return count, mid
    #         elif mid**2 > x:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return count, left - 1

    """
    이해하고 최종 버전
    "mid**2 > x" 이면 mid는 일단 큰 대상이고 그거보다 작은거 찾아야 하는데 binary로 할거니깐 일단 탈락 mid에서 1줄이고 최소값은 그대로 두고 중간값
    "mid**2 < x" 이면 mid는 일단 작은 대상이고 그거보다 큰거 찾아야 하는데 binary로 할거니깐 일단 탈락 mid에서 1올리고 최댓갑은 그대로 두고 중간값
    """
    def mySqrt2(self, x):
        count = 0
        left, right = 0, x
        while left <= right:
            count+=1
            mid = (left + right) // 2
            if mid**2 <= x < (mid+1)**2:
                return count, mid
            elif mid**2 > x:
                right = mid - 1
            else:
                left = mid + 1

"""
아주 작은 범위에서는 범위가 적으므로 제곱이 적은 수에서 1씩 증가시켜가며 찾는게 빠른 경우도 있다 하지만 범위가 엄청나게 커지는 경우엔 mySqrt2가 시간복잡도가 훨싼 더 작고, 그 차이는 수가 커지면 커질수록 커진다.
=> 1203으로 직접 해보고 알았다. 내가 짰던 알고리즘은 포인트가 된 지점의 제곱이 더 작은 경우 1씩 증가 하지만 두번째 알고리즘은 자기가 너무 많이 왔나보다 하고 "그 전것과의(마지막 최댓값과의)" 반으로 가서 서치를 하는 것 그러니 크든 작든 범위를 이전 탐색의 반만큼씩 줄였던 것이다. 
"""
s = Solution()
test1 = s.mySqrt(227)   # => count, result (5, 15)
print(1, test1)
test2 = s.mySqrt2(227)   # => count, result (8, 15)
print(2, test2)
test3 = s.mySqrt(1203)   # => count, result (5, 15)
print(3, test3)
test4 = s.mySqrt2(1203)   # => count, result (8, 15)
print(4, test4)
test5 = s.mySqrt(230000000)   # => count, result (1141, 15165)
print(5, test5)
test6 = s.mySqrt2(230000000)    # => count, result (28, 15165)
print(6, test6)





