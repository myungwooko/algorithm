"""
572. Subtree of Another Tree
Easy

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a
subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also
be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


class Solution:
    def isSubtree(self, s, t):
        # same structure is possible
        # it share exactly same with from the subtree's root node
        # can I asume there is no duplicate value in a tree?
        def isEqual(n1, n2):
            if n1 and n2:
                return n1.val == n2.val and isEqual(
                    n1.left, n2.left) and isEqual(n1.right, n2.right)
            elif any([n1, n2]):
                return False
            else:
                return True

        def dfs(n1, n2):
            if n1 and n2:
                if n1.val == n2.val and isEqual(n1, n2):
                    return True
                return isEqual(n1.left, n2) or isEqual(n1.right, n2)
            elif any([n1, n2]):
                return False
            else:
                return True

        return dfs(s, t)
