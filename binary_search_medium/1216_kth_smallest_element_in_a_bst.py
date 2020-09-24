"""
230. Kth Smallest Element in a BST
Medium

1528

50

Favorite

Share
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

- BST => lefty are smaller than righty
- node.parent is more right than node.right
- and use stack
=> that's all
=> 좌 빼고 => 부모인 자신 빼고 => (그 위의 부모로 올라가기전) 자신의 우 빼고 => 반복
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # iteratively
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            root = node.right


node2 = TreeNode(2)
node1 = TreeNode(1)
node4 = TreeNode(4)
node3 = TreeNode(3)
node1.right = node2
node3.left = node1
node3.right = node4

kth = 1
s = Solution()
test = s.kthSmallest(node3, kth)
print(test)
