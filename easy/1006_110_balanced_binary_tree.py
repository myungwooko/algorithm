"""
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

- maximum depth difference for nodes on same depth is 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root:
            return True

        return abs(self.getHeight(root.left) -
                   self.getHeight(root.right)) < 2 and self.isBalanced(
                       root.left) and self.isBalanced(root.right)

    def getHeight(self, root):
        if not root:
            return 0

        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


"""
[3,9,20,null,null,15,7] => true
[3,9,20,null,null,15,7,null, null, 3, null] => false
[3,9,20,1,2,3,4] => true
[1,null,2,null,3] => false
[1,2,2,3,3,null,null,4,4] => false
[1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5] => true
[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7] => true
[1,2,2,3,null,null,3,4,null,null,4] => false

"""

s = Solution()

# [1,null,2,null,3]
# root = TreeNode(1)
# f_right = TreeNode(2)
# f_right.right = TreeNode(3)
# root.right = f_right

# [2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]
root = TreeNode(2)
f_left = TreeNode(1)
f_right = TreeNode(3)
f_left.left = TreeNode(0)
f_left.right = TreeNode(7)
f_right.left = TreeNode(9)
f_right.right = TreeNode(1)
f_left.left.left = TreeNode(2)
f_left.right.left = TreeNode(1)
f_left.right.right = TreeNode(0)
f_left.right.right.left = TreeNode(7)
f_right.right.left = TreeNode(8)
f_right.right.right = TreeNode(8)
root.left = f_left
root.right = f_right

test = s.isBalanced(root)
print(1, test)
"""
========================================================================================================================
"""


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        current_layer = [root]
        under_whole_layer = []
        while True:
            zero = False
            for node in current_layer:
                under_layer = []
                print('current layer', [node.val for node in current_layer])
                print('node', node.val)
                if node.left:
                    under_whole_layer.append(node.left)
                    under_layer.append(node.left)
                else:
                    zero = True
                if node.right:
                    under_whole_layer.append(node.right)
                    under_layer.append(node.right)
                else:
                    zero = True

                under_depth = [self.depth(node, 0) for node in under_layer]
                under_depth.sort()
                print('under layer', [node.val for node in under_layer])
                print('under depth', under_depth)
                if zero and under_depth:
                    under_depth.insert(0, -1 * under_depth[0])

                if under_depth and under_depth[-1] - under_depth[0] > 1:
                    print('under layer', [node.val for node in under_layer])
                    print(33, under_depth)
                    return False
                print('=========')
            if not under_whole_layer:
                return True
            else:
                current_layer = under_whole_layer
                under_whole_layer = []

    def depth(self, root, depth):
        if not root.left and not root.right:
            return depth
        left = right = 0
        if root.left:
            left = self.depth(root.left, depth + 1)
        if root.right:
            right = self.depth(root.right, depth + 1)
        return max(left, right)

    #
    # def child(self, root):
    #     if root.left or root.right:
    #         return True
    #     else:
    #         return False


"""
[3,9,20,null,null,15,7] => true
[3,9,20,null,null,15,7,null, null, 3, null] => false
[3,9,20,1,2,3,4] => true
[1,null,2,null,3] => false
[1,2,2,3,3,null,null,4,4] => false
[1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5] => true
[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7] => true
[1,2,2,3,null,null,3,4,null,null,4] => false

"""

# s = Solution()

## [1,null,2,null,3]
# root = TreeNode(1)
# f_right = TreeNode(2)
# f_right.right = TreeNode(3)
# root.right = f_right

## [2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]
# root = TreeNode(2)
# f_left = TreeNode(1)
# f_right = TreeNode(3)
# f_left.left = TreeNode(0)
# f_left.right = TreeNode(7)
# f_right.left = TreeNode(9)
# f_right.right = TreeNode(1)
# f_left.left.left = TreeNode(2)
# f_left.right.left = TreeNode(1)
# f_left.right.right = TreeNode(0)
# f_left.right.right.left = TreeNode(7)
# f_right.right.left = TreeNode(8)
# f_right.right.right = TreeNode(8)
# root.left = f_left
# root.right = f_right
#
# test = s.isBalanced(root)
# print(1, test)
"""
[5,6,0,3,0,0,6,0,5,8,5,0,7,5,0,2,2,7,4,0,8,5,8,2,1,6,9,2,8,9,0,3,5,8,8,2,2,0,8,1,0,9,5,6,5,2,2,0,9,9,2,0,5,1,5,9,7,3,9,8,0,2,6,8,0,5,1,3,3,3,0,0,8,2,0,8,7,4,1,4,0,4,4,7,1,7,4,9,8
,3,2,7,7,8,5,3,0,6,7,8,9,3,9,3,6,4,4,6,4,9,4,8,3,9,1,9,8,3,2,4,3,7,1,7,0,5,3,1,3,0,3,1,4,9,3,7,5,8,6,7,2,5,6,2,3,4,0,5,1,8,6,7,7,9,5,8,0,7,6,3,9,4,8,4,6,2,2,2,5,0,7,4,0,6,9,0,7,7
,8,2,4,3,6,2,3,7,3,0,4,0,7,9,7,9,9,9,0,2,7,8,0,7,4,1,2,2,8,5,4,8,4,3,6,0,2,1,9,2,8,9,9,2,8,4,3,9,4,3,5,8,2,9,3,3,8,9,6,1,3,2,1,9,5,6,0,5,5,7,9,7,5,5,7,8,3,5,6,9,0,3,7,6,0,6,2,7,2
,7,7,6,2,9,4,3,0,0,5,5,8,9,8,3,6,8,1,1,8,5,5,2,7,8,6,9,6,6,5,7,5,8,4,6,7,7,6,5,1,1,5,6,4,1,8,8,9,4,6,2,0,9,7,5,8,5,9,9,3,0,0,3,4,5,7,8,6,1,7,2,9,0,6,1,4,8,6,7,6,4,0,4,6,7,6,0,5,1
,8,6,8,5,5,3,0,7,8,4,0,2,5,0,5,0,8,8,7,1,0,9,3,3,0,8,5,5,7,0,6,8,3,5,8,3,7,0,6,2,3,7,1,1,5,4,5,7,8,2,1,8,4,0,1,2,0,7,2,8,2,1,6,9,7,0,5,6,9,9,9,9,5,3,2,9,3,7,2,5,3,0,8,0,4,5,0,1,9,
2,6,9,1,6,4,1,3,0,6,0,9,8,9,6,0,8,9,6,6,7,7,4,7,2,5,7,2,8,9,3,0,5,4,2,9,1,1,0,8,3,8,9,2,8,0,8,3,8,4,9,9,8,5,2,3,0,9,2,7,4,0,2,0,3,3,2,5,0,8,4,5,6,7,7,6,8,7,8,8,3,3,0,4,0,1,2,7,1,
null,3,8,3,8,5,5,2,null,3,3,6,6,9,5,4,null,5,2,5,null,6,8,2,8,8,0,3,null,7,8,7,null,8,6,3,5,5,4,7,4,6,8,6,null,8,6,6,null,8,3,3,0,2,null,null,null,9,3,7,null,9,null,null,null,1,6,
5,6,0,0,7,2,4,7,2,7,5,3,2,0,0,9,4,8,0,0,8,null,3,3,6,6,3,0,5,1,4,4,2,6,3,9,1,null,2,9,8,5,4,5,7,4,5,6,6,8,0,2,2,null,0,7,7,7,8,null,null,null,3,0,6,1,4,4,6,3,5,null,null,null,0,5,
7,1,2,6,7,null,6,6,6,null,5,null,0,null,9,6,8,9,4,2,1,8,1,null,null,null,8,2,0,3,5,3,8,0,2,null,3,null,5,null,7,null,1,null,null,null,2,6,3,8,5,null,null,null,1,6,4,1,6,7,9,5,1,6,
7,null,6,8,4,2,7,8,3,6,2,null,null,null,5,8,7,5,8,null,0,null,5,null,null,null,3,4,8,3,2,7,7,9,2,2,5,9,9,4,9,0,8,7,2,null,4,null,null,null,1,2,2,2,0,0,1,null,0,0,6,7,9,5,3,8,8,0,1,
9,6,2,7,null,9,7,3,2,0,null,7,null,2,5,5,6,7,9,8,null,9,4,7,9,4,5,2,5,1,4,0,6,8,3,5,null,4,0,3,4,5,0,6,4,6,0,2,8,4,6,4,1,9,0,5,5,5,7,7,7,7,null,6,null,7,null,1,null,6,null,null,null,
3,4,1,4,1,1,2,7,8,3,7,null,0,0,7,2,2,7,5,3,6,6,7,0,4,2,4,6,8,5,5,3,6,5,7,null,7,null,2,null,5,3,5,1,6,4,4,null,5,6,1,9,7,4,7,5,null,null,null,null,4,6,9,4,7,8,5,4,5,9,5,null,5,null,
9,null,5,6,6,1,0,null,6,null,4,4,3,null,3,8,3,4,2,7,2,9,0,9,8,8,2,5,8,null,8,null,1,null,6,6,4,0,9,3,9,7,4,1,6,2,2,7,3,1,4,6,1,null,3,1,0,null,6,4,2,4,2,7,7,0,null,null,null,null,
null,null,null,null,8,null,null,null,8,null,null,null,4,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,4,null,null,null,3,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,3,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,3,null,null,null,null,null,null,null,3,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,9,null,5,null,9,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,null,null,null,null,null,2,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,null,5,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,3,0,0,null,null,null,6,null,null,null,9,null,
null,null,6,null,null,null,6,null,null,null,null,null,1,null,null,null,6,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,3,1,null,
null,null,null,null,0,null,null,null,null,null,null,null,null,null,2,null,null,null,0,null,null,null,9,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,3,null,null,null,8,null,null,null,null,null,0,null,null,null,1,null,6,null,6,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null
,null,null,null,null,null,null,null,null,null,null,null,null,3,null,null,null,8,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0,2,0,0,null,null,null,null,null,null,null,null,null,null,null,null,null,null
,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null
,null,2,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null
,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,4,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,5,null,null,null,9,null,3,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,6,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null
,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,2,null,7,
null,2,null,5,null,null,null,null,null,null,null,5,null,2,null,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,7,null,null,null,6,null,null,null,null,null,null,null,null,null,null,null,null,null,9,null,null,null,null,null
,null,null,null,null,null,null,null,null,null,null,4,null,null,null,3,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null
,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,3]
여기서! 아예 다르게 접근해야한다는 생
"""
