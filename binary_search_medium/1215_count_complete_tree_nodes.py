"""
222. Count Complete Tree Nodes
Medium

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
           1
       /      \
      2        3
     / \      / \
   4   5     6   7
  /\  / \   / \
 8 9 10 11 12 13

Output: 6

mine
=> see picture or draw tree when it is tricky to understand

- if "height of node.left and height of node.right are same"
    result_count + under the node.left and node then => node = node.right !!! 2**l is not only include nodes number of under the node.left and node.left but also node.
  else:
    result_count + under the node.right and node then => ndoe = node.left !!! 2**r is not only include nodes counts of under the node.right and node.right but also node.
"""
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0
        while root:
            l, r = map(self.height, (root.left, root.right))
            if l == r:
                count += 2**l
                root = root.right
            else:
                count += 2**r
                root = root.left
        return count

    def height(self, node):
        if not node:
            return
        h = 0
        while node:
            h += 1
            node = node.left
        return h







