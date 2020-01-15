"""
21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# sorted 하게 엮는 것
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

## Test해보면 알수있다. sorted 하게 엮어서 return 것
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         l = ListNode(1)
#         l.next = ListNode(1)
#         l.next.next = ListNode(2)
#         l.next.next.next = ListNode(7)
#         l.next.next.next.next = ListNode(4)
#         l.next.next.next.next.next = ListNode(9)
#         return l

# before
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         if not l1 or not l2:
#             return l1 or l2

#         sorted = []
#         flag = ""

#         while l1 and l2:
#             if l1.val <= l2.val or not l2:
#                 sorted.append(l1.val)
#                 l1 = l1.next
#                 if l1 == None:
#                     flag = "l1"
#             elif l2.val < l1.val or not l1:
#                 sorted.append(l2.val)
#                 l2 = l2.next
#                 if l2 == None:
#                     flag = "l2"

#         ret = tmp = ListNode(sorted[0])

#         for s in sorted[1:]:
#             node = ListNode(s)
#             tmp.next = node
#             tmp = tmp.next

#         if flag == "l1":
#             tmp.next = l2
#         else:
#             tmp.next = l1
#         return ret


