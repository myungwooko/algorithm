"""
338. Counting Bits
Medium

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

-  2의 거듭제곱인지 판별법: x&(x-1) == 0 true false의 결과가 2의 거듭제곱(제곱수)인지에 대한 결과
-  이진법 shift게산 법
   => n>>m : n이라는 수를 2진법으로 바꿔서 >> or << 이 가리키는 방향으로 m만큼 밀어준다. 그리고 그결과를 십진법의 수로 바꿔주면 그것이 n>>m의 결과가 된다.
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        count = 0
        for i in range(num + 1):
            li = list(str(self.change_binary(i)))
            for j in li:
                if j == "1":
                    count += 1
            res.append(count)
            count = 0
        return res

    def change_binary(self, n):
        result, idx = 0, 0
        while (n >= 1):
            n, r = divmod(n, 2)
            result += (10 ** idx) * r
            idx += 1
        return result

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(1, num+1):
            result.append(result[i>>1] + int(i&1))
        return result

s = Solution()
test = s.countBits(168)
print(test)
