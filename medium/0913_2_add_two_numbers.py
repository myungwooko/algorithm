"""
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """이게 신의 한수 cur은 그때그때의 node를 생성하기도 위하면서 처음에 dummy를 바라볼수 있게 하는 역할로서의 중추역할
       이렇게 하면 완전히 같은 것을 바라보는 것으로서 완전히 같은게 된다.
    """
    dummy = cur = ListNode(0)
    carry = 0
    """while의 or carry가 있는 이유는 없을경우 l1, l2가 한자리인 경우 다음자리가 생성되는데 그걸 처리하지 못하게 되기 때문에"""
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        """cur.next하면 맨 처음에는 동시에 dummy.next도 되는 것이다. dummy = cur 이니까"""
        cur.next = ListNode(carry % 10)
        """
        붙이고 cur.next 자체가 cur이라는 참조값의 주체가 된다. 그래서 그렇게 다음 것들을 계속 붙여나갈 목적으로서.
        즉 cur의 참조값은 바뀌게 된다. cur.next의 값으로
        """
        cur = cur.next
        carry //= 10
    """dummy.next 부터 값이 추가 되었으니깐 이렇게 하면 결과값 리턴"""
    return dummy.next


node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

a = addTwoNumbers(node1, node4)
print(a.val, a.next.val, a.next.next.val)
