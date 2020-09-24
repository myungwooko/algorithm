"""
107. Binary Tree Level Order Traversal II
Easy

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]


- DEBUG MODE를 쓰자!!!!!!!!!!!!!!!!!!!
- 모든걸 다 받는(데이터 축적) 리스트는 처음에 정의하고 recursion에 넣으면 되네 => 들어오는 그것에 항상 축적되게 정의하면 되고
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return root

        result = []
        currentLayer = [root]
        underLayer = []
        while True:
            result.append(currentLayer)
            for node in currentLayer:
                if node.left:
                    underLayer.append(node.left)
                if node.right:
                    underLayer.append(node.right)

            if not underLayer:
                break
            currentLayer = underLayer
            underLayer = []

        for i, v in enumerate(result):
            for si, sv in enumerate(v):
                v[si] = sv.val

        result.reverse()

        return result

    def levelOrderBottom1(self, root):
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if root:
            if len(
                    res
            ) < level + 1:  #==================================> 다음 층위것들이 들어왔을때를 의미 하나당 한층위의 것들이니깐
                res.insert(0, [])
            res[-(level + 1)].append(root.val)
            self.dfs(root.left, level + 1, res)
            self.dfs(root.right, level + 1, res)


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

test = s.levelOrderBottom1(root)
print(test)
