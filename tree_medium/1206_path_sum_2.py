"""
113. Path Sum II
Medium

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        path = []
        candidates = self.helper(root, path, res)
        result = []
        for i in candidates:
            if sum(i) == sum1:
                result.append(i)
        return result

    def helper(self, root, path, res):
        path.append(root.val)
        if not root.left and not root.right:
            res.append(path)
        path1 = path[:]
        path2 = path[:]
        if root.left:
            self.helper(root.left, path1, res)
        if root.right:
            self.helper(root.right, path2, res)
        return res

