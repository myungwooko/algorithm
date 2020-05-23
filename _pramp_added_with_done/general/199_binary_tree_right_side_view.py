"""
199. Binary Tree Right Side View
Medium

1798

102

Add to List

Share
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        levels = {}

        def helper(node, level):
            if level in levels:
                levels[level].append(node.val)

            levels[level] = [node.val]

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        if root:
            helper(root, 1)
        return [l[-1] for l in levels.values()]

    def rightSideView(self, root):
        res = []
        nextLev = [root] if root else []

        while nextLev:
            res.append(nextLev[-1].val)
            curLev, nextLev = nextLev, []
            for node in curLev:
                if node.left: nextLev.append(node.left)
                if node.right: nextLev.append(node.right)
        return res


