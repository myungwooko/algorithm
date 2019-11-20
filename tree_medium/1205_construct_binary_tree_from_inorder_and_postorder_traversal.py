"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7



inorder => 좌 -> 자신 -> 우
postorder => 좌 -> 우 -> 자신
각각을 이용할땐 각각의 룰에 입각해서 이용하면 된다.
- postorder는 뒤에서 부모 -> 우 -> 좌의 순서로 갈 것이고
- inorder는 노드기준 왼쪽에 있으면 좌, 오른쪽에 있으면

- right first because postorder's reverse sequence is root -> right -> left
- inorder => left is left, right is right
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root