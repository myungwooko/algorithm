"""
103. Binary Tree Zigzag Level Order Traversal
Medium

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root
        res = []
        self.helper(root, res, 0)
        return res

    def helper(self, node, res, level):
        while level == len(res):
            res.append([])
        if type(node.val) == int:
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)
        if node.left is not None:
            self.helper(node.left, res, level + 1)
        if node.right is not None:
            self.helper(node.right, res, level + 1)

    def zigzagLevelOrder1(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) < level + 1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(curr.val)
                else:
                    res[level].insert(0, curr.val)
                queue.append((curr.left, level + 1))
                queue.append((curr.right, level + 1))
        return res
