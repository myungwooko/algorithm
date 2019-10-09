"""
101. Symmetric Tree
Easy

2682

60

Favorite

Share
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.


*********************************************************************
- check PLEASE execptional cases => input is []   !!!
- Remember that easy format for tree's dfs' recursive function .
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        up_nodes = [root]
        under_nodes = []
        under_vals = []

        while True:
            for node in up_nodes:
                if node.left:
                    under_nodes.append(node.left)
                    under_vals.append(node.left.val)
                else:
                    under_vals.append("False")
                if node.right:
                    under_nodes.append(node.right)
                    under_vals.append(node.right.val)
                else:
                    under_vals.append("False")

            print(1, under_vals)
            if under_vals[0] == "False" and len(set(under_vals)) == 1:
                return True

            if len(under_nodes)%2:
                return False
            else:
                half = len(under_vals) // 2
                left = under_vals[0:half]
                right = under_vals[half:len(under_vals)]
                right.reverse()

                if left == right:
                    up_nodes = under_nodes
                    under_nodes = []
                    under_vals = []
                else:
                    return False

    def isSymmetric2(self, root):
        if not root:
            return True
        return self.dfs(root.left, root.right)


    def dfs(self, a, b):
        if a and b:
            return a.val == b.val and self.dfs(a.left, b.right) and self.dfs(a.right, b.left)
        return a is b



"""
    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""


root = TreeNode(1)
fd_left = TreeNode(2)
# fd_left.left = TreeNode(3)
fd_left.right = TreeNode(3)
root.left = fd_left
fd_right = TreeNode(2)
fd_right.left = TreeNode(3)
# fd_right.right = TreeNode(3)
root.right = fd_right

s = Solution()
print(1, s.isSymmetric(root))













