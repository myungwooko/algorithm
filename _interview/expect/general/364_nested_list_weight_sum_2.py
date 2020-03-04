"""
364. Nested List Weight Sum II
Medium

468

119

Add to List

Share
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up.
i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's at depth 1, one 2 at depth 2.
Example 2:

Input: [1,[4,[6]]]
Output: 17
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:

    # weight means depth => start from innerest one with 1
    # Time O(NlogN) because of sort()
    def depthSumInverse(self, nestedList):

        nAD = []

        def helper(nl, depth):
            curr = []
            nums = []
            for e in nl:
                if e.isInteger():
                    nums.append(e.getInteger())
                else:
                    helper(e.getList(), depth + 1)
            curr.append(nums)
            curr.append(depth)
            nAD.append(curr)
            return

        helper(nestedList, 1)

        depths = set()
        for nums, d in nAD:
            depths.add(d)

        depths = list(depths)
        depths.sort()

        l = 0
        r = len(depths) - 1
        mapDepth = {}
        while l <= r:
            mapDepth[depths[l]] = depths[r]
            mapDepth[depths[r]] = depths[l]
            l += 1
            r -= 1

        multiplied = [sum(nums) * mapDepth[dK] for [nums, dK] in nAD]

        return sum(multiplied)

    # simpler and faster
    # Time O(NlogN) because of sort()
    def depthSumInverse(self, nestedList):

        # sum and reversed depth
        sAR = []
        depths = []

        def helper(nl, depth):
            depths.append(depth)
            curr = []
            for e in nl:
                if e.isInteger():
                    curr.append(e.getInteger())
                else:
                    helper(e.getList(), depth + 1)

            sAR.append([sum(curr), depth])
            return

        helper(nestedList, 1)
        maxDepth = max(depths)
        sAR.sort(key=lambda x: x[1], reverse=True)

        idx = 1
        while idx < len(sAR):
            if sAR[idx - 1][1] == sAR[idx][1]:
                sAR[idx][0] += sAR[idx - 1][0]
                sAR.pop(idx - 1)
            else:
                idx += 1

        return sum([sAR[i - 1][0] * i for i in range(1, maxDepth + 1)])
