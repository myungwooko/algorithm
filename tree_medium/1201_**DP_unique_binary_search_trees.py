"""
96. Unique Binary Search Trees
Medium

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

explanation
- youtube.com/watch?v=YDf982Lb84o
=> 왜 곱하지?

ex)
=> 10,11,12,13

=> 10이 루트인 경우 왼쪽은 0개 오른쪽은 3개를 가지고 만들수 있는 경우의 수 카운트.
=> 0개인 거는 카운트 할 필요없고, => 이것을 default 1로 하기위해서 res[0] => node 하나만 있어도 일단 구조하나는 나오니깐 그냥 하나있는 구조.
=> 오른쪽 3개는 카운트
=> 1 x 3 => 3

=> 11이 루트인 경우 왼쪽에선 1개, 오른쪽은 2개를 가지고 만들수 있는 경우의 수 카운트.
=> 왼쪽에서 만들수 있는 1 X 오른쪽에서 만들수 있는 2 를 곱한것이
=> 해당 루트 11에 대한 모든 경우의 수이다.
=> 왜냐하면 각각 1개, 2개 인건데 오른쪽의 두가지의 다른 모양의 경우 각각에 대해 왼쪽의 1은 모두 조합을 가질수 있으므로 1X2가 된다.
=> 1 x 2 => 2

go on... + case of root 12 + case of root 13

그러면 답.


- youtube.com/watch?v=YDf982Lb84o
*** simpler explanation of mine ***
- index of res indicate number of tree node and value of res[index] indicate => number of possible tree structure
- the problem said "1...n" so it starts from 1 even though n is 0.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # simple DP => understanding of DP.
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n + 1)
        res[0] = 1
        print(1, res)
        for i in range(1, n + 1):
            for j in range(i):
                print(11, res)
                # j = left side, i-1-j = right side
                # => what is i-1-j => left + right + the root(turn of this time) is total n
                # => that means firstly right side should minus 1 because it shouldn't include root
                # => and also right side shouldn't include left side count
                # => that naturally made i-1-j => 1=root count, j=left side count
                res[i] += res[j] * res[i - 1 - j] # this easily counts all of combinations for making n nodes unique structure Trees.
                print(22, i, j, i-1-j)
                print(33, res[j], res[i-1-j])
        print(4, res)
        return res[n]

    #only code
    def numTrees(self, n):
        res = [0] * (n + 1)
        res[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                res[i] += res[j] * res[i - 1 - j]
        return res[n]

s = Solution()
test = s.numTrees(4)
print(test)









