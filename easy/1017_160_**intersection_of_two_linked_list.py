"""
160. Intersection of Two Linked Lists
Easy

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def getIntersectionNode(self, headA, headB): =====================================> Time Limit Exceed
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         if not headA or not headB:
#             return
#
#         vals = []
#         curA = headA
#         curB = headB
#
#         while curA:
#             vals.append(curA)
#             curA = curA.next
#
#         while curB:
#             if curB in vals:
#                 return curB
#             curB = curB.next
#
#         return
"""
If two linked lists have intersection, we can find two observations:

They must have same nodes after the intersection point.
L1+L2 must have same tail from the intersection point as L2 + L1. For example,
L1 = 1,2,3
L2 = 6,5,2,3

L1+L2 = 1,2,3,6,5,2,3
L2+L1 = 6,5,2,3,1,2,3

왜냐면 둘다 어딘가에서는 만나고 거기서부턴 똑같이 가서 끝나는 건 똑같기 때문에
위와 같이 더하면 길이는 같아지고 접합지점 부터의 모습을 같게 힐수 있다. 
그래서 아래의 함수는 둘을 더해서 만나는 지점인 꼬리부분으로 들어갈떄 둘은 같아지고 그때 그것을 리턴하면 된다는 논리.

아래의 함수 while loop에서 2에서 나가게 되고 그 node를 리턴
1-2-3-None-6  -5-(2)-3
6-5-2-  3-None-1-(2)-3


그리고 마찬가지로 둘이 같은게 없을때도 위를 그대로 따라가 길이는 같아지고 같은게 없고 마지막 한번더 None==None으로 while loop을 빠져 나가게 되고 그 node를 리턴 
L1 = 1,2,3
L2 = 4,5,6,7
1-2-3-None-4-5-6-7-(None)
4-5-6-7-None-1-2-3-(None)





"""


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = headB if not p1 else p1.next
            p2 = headA if not p2 else p2.next
        return p1


a = ListNode(1)
a.next = ListNode(2)

b = ListNode(7)
b.next = ListNode(8)

s = Solution()
test = s.getIntersectionNode(a, b)
print(11, test)
