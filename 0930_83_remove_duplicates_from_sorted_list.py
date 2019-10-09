"""
83. Remove Duplicates from Sorted List
Easy

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

**********************************************************
!!! should handle this execptional situation => head => []
**********************************************************
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dup_res = []
        cur = head
        while cur.next != None:
            dup_res.append(cur.val)
            cur = cur.next
        dup_res.append(cur.val)
        res = list(set(dup_res))
        res.sort()
        print(res)
        result = cur = ListNode(res[0])
        for i in range(1, len(res)):
            cur.next = ListNode(res[i])
            cur = cur.next
        return result

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        """
        leetcode 100% => this is better
        :param head:
        :return:
        """
        if not head:
            return head
        result = cur = head
        while cur.next != None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return result


a = ListNode(-1)
a.next = ListNode(0)
a.next.next = ListNode(3)
a.next.next.next = ListNode(3)

# while a.next != None:
#     print(a.val)
#     a=a.next
# print(a.val)

s = Solution()
test = s.deleteDuplicates(a)
print(test)
while test.next != None:
    print(test.val)
    test=test.next
print(test.val)


a = ListNode(-1)
a.next = ListNode(0)
a.next.next = ListNode(3)
a.next.next.next = ListNode(3)

# while a.next != None:
#     print(a.val)
#     a=a.next
# print(a.val)

s = Solution()
test = s.deleteDuplicates2(a)
print(test)
while test.next != None:
    print(test.val)
    test=test.next
print(test.val)






