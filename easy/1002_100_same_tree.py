"""
100. Same Tree
Easy

1331

43

Favorite

Share
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
"""
************************************************************************************************************************
- Concern case of input is [] 
- the below solution's else clause checks whether it is same as None and None or not as some value and None at the end. => not => False
- and if clause checks whether values are same or not and trigger recursive functions for left values and right values each.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(
                p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)

t2 = TreeNode(1)
t2.right = TreeNode(3)

t3 = TreeNode(None)
t4 = TreeNode(None)

s = Solution()
test = s.isSameTree(t3, t4)
print(test)
