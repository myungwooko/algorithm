"""
237. Delete Node in a Linked List
Easy

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:





Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.


Note:
The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        print(node)
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


def shortestCellPath(grid, sr, sc, tr, tc):
    if not grid or not grid[0]:
        return -1
    m = len(grid)
    n = len(grid[0])

    queue = [(sr, sc, 0, [])]
    while queue:
        r, c, count, seen = queue.pop(0)
        if r == tr and c == tc:
            return count
        candidates = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]
        for r1, c1 in candidates:
            if 0 <= r1 < m and 0 <= c1 < n and grid[r1][c1] and (r1, c1) not in seen:
                queue.append((r1, c1, count + 1, seen + [(r1, c1)]))

    return -1


grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0
sc = 0
tr = 2
tc = 0

test = shortestCellPath(grid, sr, sc, tr, tc)
print(test==8)










