"""
543. Diameter of Binary Tree
Easy

1980

122

Add to List

Share
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def depth(p):
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            # 이렇게 되면 왼쪽으로도 최소 1 더해진거, 플러스 오른쪽으로도 최소 1 더해진것으로서 count가 맞다.
            self.ans = max(self.ans, left + right)
            #+1을 해주는 이유는 최소 자기로부터의 거리를 재야 하니까, 숫자를 return해주는 이유? 그래야 depth를 알고 비교해주니까.
            return 1 + max(left, right)
        depth(root)
        return self.ans
