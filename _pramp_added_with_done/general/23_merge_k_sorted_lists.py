"""
23. Merge k Sorted Lists
Hard

3596

228

Add to List

Share
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        dummy = curr = ListNode(0)

        vals = []
        idx = 0
        while idx < len(lists):
            while lists[idx]:
                vals.append(lists[idx].val)
                lists[idx] = lists[idx].next
            idx += 1

        heapq.heapify(vals)
        while vals:
            val = heapq.heappop(vals)
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
