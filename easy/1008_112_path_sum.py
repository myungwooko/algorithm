"""
112. Path Sum
Easy

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum_list = []
        acc = 0
        self.sum_under(root, acc, sum_list)
        if sum in sum_list:
            return True
        else:
            return False

    def sum_under(self, node, acc, acc_list):
        if not node:
            return
        acc += node.val
        if not node.left and not node.right:
            acc_list.append(acc)

        if node.left:
            self.sum_under(node.left, acc, acc_list)
        if node.right:
            self.sum_under(node.right, acc, acc_list)


"""
test case
- [1,2], 1 => false
- [5,4,8,11,null,13,4,7,2,null,null,null,1], 22 => true

"""
