"""
147. Insertion Sort List
Medium

Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list


Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        resList = []
        cur = head
        while cur:
            if not resList:
                resList.append(cur.val)
            else:
                inserted = False
                for i, v in enumerate(resList):
                    if cur.val < v:
                        resList.insert(i, cur.val)
                        inserted = True
                        break
                if not inserted:
                    resList.append(cur.val)
            cur = cur.next
        result = currNode = ListNode(resList[0])
        for i in range(1, len(resList)):
            nextNode = ListNode(resList[i])
            currNode.next = nextNode
            currNode = nextNode
        return result

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
test = s.insertionSortList(input1)
resultList = s.LinkedListToList(test)
print(resultList)



