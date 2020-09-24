"""
114. Flatten Binary Tree to Linked List
Medium

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        res = []
        self.dfs(root, res)
        root.left = None
        cur = root
        for i in range(1, len(res)):
            val = res[i]
            cur.right = TreeNode(val)
            cur = cur.right
        return root

    def dfs(self, root, res):
        if not root:
            return
        res.append(root.val)
        if root.left:
            self.dfs(root.left, res)
        if root.right:
            self.dfs(root.right, res)
        return

    # recusively
    def flatten1(self, root):
        self.helper(root)

    def helper(self, root):
        if not root:
            return
        # You can draw the each recursion process inside and can connect it.
        # 왼쪽으로 끝까지 내려가고 하나가 자신자체를 해당 node의 left child로 뱉어내는 그 층에서 => 결국 자식 하나의 부모가 root node가 된다. => 거기서 부터 시작
        # 왼쪽의 마지막을 집었으면 오른쪽떼고 붙이면 되는 거니까 붙이면 된다.
        # 오른쪽도 일련의 과정을 한것으로서 존재하는 것이니.
        # 붙일때 left의 tail에 right을 붙여야 하고
        # left 자리는 꺠끗하게 청소해준다.
        l = self.helper(root.left)
        r = self.helper(root.right)
        if l:
            root.right = l
            # to indicate the tail to attach the right
            # 결국 붙일땐 들어가고 들어가서 안쪽에서 부터 완룍 된것으로 붙여져있는 것이므로 left의 존재여부는 고려할 필요없다. => 다 오른쪽으로 붙여져 있는 것이므로.
            while l and l.right:
                l = l.right
            l.right = r
            root.left = None  # take care here
        return root
