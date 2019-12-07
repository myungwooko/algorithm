"""
173. Binary Search Tree Iterator
Medium

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.



Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.helper(root)

    def helper(self, root):
        if not root:
            return

        if not self.stack:
            self.stack.append(root.val)
        else:
            insert = False
            for i, v in enumerate(self.stack):
                if v < root.val:
                    self.stack.insert(i, root.val)
                    insert = True
                    break
            if not insert:
                self.stack.append(root.val)
        if root.left:
            self.helper(root.left)
        if root.right:
            self.helper(root.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.stack.pop()

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if not self.stack:
            return False
        else:
            return True

"""
Because binary search tree's lefty nodes are always lesser than their righty nodes.
"""
class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.helper(root)

    def helper(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return self.stack != []

    def next(self):
        node = self.stack.pop()
        self.helper(node.right)
        return node.val


