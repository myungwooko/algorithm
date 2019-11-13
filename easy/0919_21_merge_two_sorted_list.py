"""
21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
"""
- a or b => a와 b의 합집합이 return
- 반복에서의 recursion 이용은 아래 참고.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1  or not l2:
            return l1 or l2

        sorted = []
        flag = ""
        while l1 and l2:
            if l1.val <= l2.val or not l2:
                sorted.append(l1.val)
                l1 = l1.next
                if l1 == None:
                    flag = "l1"
            elif l2.val < l1.val or not l1:
                sorted.append(l2.val)
                l2 = l2.next
                if l2 == None:
                    flag = "l2"

        ret = tmp = ListNode(sorted[0])
        for s in sorted[1:]:
            node = ListNode(s)
            tmp.next = node
            tmp = tmp.next

        if flag == "l1":
            tmp.next = l2
        else:
            tmp.next = l1

        return ret

"""
참고한 reecursive 풀이
결과가 recursive하게 들아가면서 연결이 되어지게 되는.
"""
# recursively
# def mergeTwoLists2(self, l1, l2):
#     if not l1 or not l2:
#         return l1 or l2
#     if l1.val < l2.val:
#         l1.next = self.mergeTwoLists(l1.next, l2)
#         return l1
#     else:
#         l2.next = self.mergeTwoLists(l1, l2.next)
#         return l2

