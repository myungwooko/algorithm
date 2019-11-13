# Definition for a binary tree node.
"""
- number of nodes(including root node) along the shortest path from root to one of the nearest leaf
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        current_layer = [root]
        under_layer = []
        depth = 0

        while True:
            for node in current_layer:
                count = 0
                if node.left:
                    under_layer.append(node.left)
                    count += 1
                if node.right:
                    under_layer.append(node.right)
                    count += 1
                if not count:
                    return depth+1
            depth += 1

            current_layer = under_layer
            under_layer = []


"""
testcase
- [3,9,20,null,null,15,7] => 2
- [1,2] => 2
- [1,2,3,4,5] => 2
"""
