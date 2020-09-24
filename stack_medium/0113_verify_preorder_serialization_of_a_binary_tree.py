"""
331. Verify Preorder Serialization of a Binary Tree
Medium

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: "1,#"
Output: false
Example 3:

Input: "9,#,#,1"
Output: false

- 마지막이 모두 #로 끝맺음 되어야 한다.
"""


class Solution(object):
    #every last has to finish "#""
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for c in preorder.split(','):
            stack.append(c)
            print(stack, stack[:-2])
            while stack[-2:] == ['#', '#']:
                stack.pop()
                stack.pop()
                if not stack: return False
                # even though just below value is '#' it doesn't matter
                stack.pop()
                #this is for next's child as finishing well as before.
                stack.append('#')
        print(stack)
        return stack == ['#']


preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
s = Solution()
test = s.isValidSerialization(preorder)
print(test)
