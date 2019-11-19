"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

Algorithm
@preorder = 어쨌든 층의 순서
@inorder를 기준으로 tree를 만들어 나간다.
=> res = preorder.index() == 0 인것 ==> 마지막에 return res

inorder
=> 가장 왼쪽에서 시작하고,
1. 이전것보다 높은층이면 이전것을 left로 가지는 부모
2. 이전것보다 낮은 층이면
 if 다음것이 자신 보다 높은 층인 경우 그것의 left로서 가고 해당 다음것을 이전것의 right로
 else 다음것이 자신보다 높은 층이 아닌경우 이전것의 right로 간다.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        @param preorder, a list of integers
        @param inorder, a list of integers
        @return a tree node
        """
        if not preorder or not inorder:
            return None

        rootVal = preorder.pop(0)
        root = TreeNode(rootVal)
        inorderIdx = inorder.index(rootVal)

        root.left = self.buildTree(preorder, inorder[:inorderIdx])
        root.right = self.buildTree(preorder, inorder[inorderIdx + 1:])

        return root


















