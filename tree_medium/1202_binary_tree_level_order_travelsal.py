"""
102. Binary Tree Level Order Traversal
Medium

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root
        res = []
        self.helper(root, res, 0)
        return res

    def helper(self, node, res, levelIdx):
        while levelIdx == len(res):
            res.append([])
        if type(node.val) == int:
            res[levelIdx].append(node.val)
        else:
            return
        if node.left:
            self.helper(node.left, res, levelIdx+1)
        if node.right:
            self.helper(node.right, res, levelIdx+1)



















