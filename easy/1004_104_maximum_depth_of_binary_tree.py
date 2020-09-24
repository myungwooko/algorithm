"""
104. Maximum Depth of Binary Tree
Easy

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.\

********************************************************************************************************************
- for loop은 for 대상이 되는 iterated 되는 것은 for loop내에서 그 메모리에 다른 것을 중간에 할당해도 for loop의 iterated 되는 주체는 처음 것 그대로 유지된다. 하지만 for loop내에서는 그 메모리는 변경된 것으로 적용된다.
=> 즉, for loop 대상은 처음에 하면 그걸로 끝, 안에서 바꾸면 안에서 바꾼 내용은 내부에서만 적용.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = 0
        currentLayer = [root]
        underLayer = []

        while currentLayer:
            depth += 1
            for node in currentLayer:
                if node.left:
                    underLayer.append(node.left)
                if node.right:
                    underLayer.append(node.right)

            currentLayer = underLayer
            underLayer = []

        return depth

    def maxDepth2(self, root):
        return 1 + max(map(self.maxDepth2,
                           (root.left, root.right))) if root else 0


"""
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3
"""
s = Solution()

root = TreeNode(3)
f_left = TreeNode(9)
f_right = TreeNode(20)
s_left = TreeNode(15)
s_right = TreeNode(7)

f_right.left = s_left
f_right.right = s_right

root.left = f_left
root.right = f_right

test = s.maxDepth(root)
print(test)
