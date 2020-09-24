"""
148. Sort List
Medium

1865

97

Favorite

Share
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5



In merge에서
- l과 pre는 따로 존재하는 것.
- pre는 계속 증가해 나간다. l이 pre보다 하나 앞서가는 개념인데
    pre는 if와 else에 상관없이 한번씩 무조건 다음으로 나아가는데
    => if 에서 l이 하나씩 증가하면 pre도 하나씩 증가해서 간격(pre, l)을 유지하고
    => else 에서 r의 비교대상을 pre뒤에 붙이면 -> l은 pre와 간격이 2가 되므로 pre가 한칸을 앞으로 나가서 원래의 간격을 유지한다. 여기서 l이 가리키는 것을 그대로 유지되는 개념.
- fast, slow = head.next, head 가 아니라 fast, slow = haed, head 이렇게하면 head가 [num1, num2] 이렇게 두개 들어오는 경우 똑같은거 계속 반복 head가 다시 [num1, num2]가 되기 때문.
  => fast, slow = head.next, head 이렇게 하면 두개가 들어왔을때도 두개를 하나 하나로 쪼개개 된다.

- r이 커서 붙여도 l애 붙이고 r을 기존 r의 next로 시작해도
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        # divide list into two parts
        fast, slow = head.next, head
        print(123, slow.val, fast.val)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        # cut down the first part
        slow.next = None
        print(self.LinkedListToList(head), self.LinkedListToList(second))
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    # merge in-place without dummy node
    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        # get the return node "head"
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else:
                # at this point it is as same as "l" but not l(l is not referencing this so "l" won't be changed)
                nxt = pre.next
                pre.next = r
                tmp = r.next
                r.next = nxt
                r = tmp
            pre = pre.next
        # l and r at least one is None
        pre.next = l or r
        return head

    @staticmethod
    def makingLinkedList(nums):
        if not nums:
            return nums
        result = currNode = ListNode(nums[0])
        for i in range(1, len(nums)):
            nextNode = ListNode(nums[i])
            currNode.next = nextNode
            currNode = nextNode
        return result

    @staticmethod
    def LinkedListToList(tree):
        res = []
        cur = tree
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return res


s = Solution()
input = s.makingLinkedList([])
input1 = s.makingLinkedList([4, 2, 1, 3])
test = s.sortList(input1)
resultList = s.LinkedListToList(test)
print(resultList)
