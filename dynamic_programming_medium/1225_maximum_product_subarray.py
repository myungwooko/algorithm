"""
152. Maximum Product Subarray
Medium

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

- contiguos 니까 음수도 마지막에 음수만나서 큰 양수가 될수 있는 것이니 일단 끝까지는 해봐야 아는 것이고,
- 계속 더해나가면서 얼마나 어떻게 커질지를 확인하며 쭉 저장해놓는 것
- 양쪽에서 다 확인을 해야 한다. 어떤식으로 어떻게 끊기고(그때까지 큰걸 뽑아내고나서) 계속 음수일수 있는데 앞과 뒤는 각각 앞지점에서 먼저 계산 된 다른 큰걸 가질 수 있으므로
- 중간에 음수로 바뀌어서 끊겨도 그 전의 것은 저장 되어있기 때문에 상관없고
- 나중에 음수 한번 더 만나서 작아질 애는 계속 해나가봐야 알수 있고, 일단 그 전까지의 큰 것은 그 지점에 계산해서 저장한다. 설사 그 다음 음수로 끝나는 애라고 하더라도. so 상관없음.
- 다른 수에 대한 0은 계산에선 건너뛴다.
- 0자체는 자신의 순서에 대해선 자신으로서 저장 되므로 카운팅 됨.
"""


class Solution(object):
    def maxProduct(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)


input = [2, 3, -2, 4]
input = [7, -4, 3, 1, 1]
s = Solution()
test = s.maxProduct(input)
print(test)
