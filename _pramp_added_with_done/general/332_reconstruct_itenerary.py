"""
332. Reconstruct Itinerary
Medium

1265

792

Add to List

Share
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order.
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

# Every ticket can't be valid answer for that turn
# So we need to check everything
# [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# In this case
# => if we choose ["JFK","KUL"] as the first one(because it is prior to ["JFK","NRT"] in lexical order)
# => it can't make valid answer
from collections import deque, defaultdict

# Every ticket can't be valid answer for that turn
# So we need to check everything
# [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# In this case
# => if we choose ["JFK","KUL"] as the first one(because it is prior to ["JFK","NRT"] in lexical order)
# => it can't make valid answer

# Every ticket can't be valid answer for that turn
# So we need to check everything
# [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# In this case
# => if we choose ["JFK","KUL"] as the first one(because it is prior to ["JFK","NRT"] in lexical order)
# => it can't make valid answer
import collections


class Solution(object):
    def findItinerary(self, tickets):
        n = len(tickets)
        revLexTickets = sorted(tickets)[::-1]
        revIdMap = collections.defaultdict(list)

        for i, (d, a) in enumerate(revLexTickets):
            revIdMap[d].append(i)

        # print(graph)
        stack = [["JFK", [], []]]

        while stack:
            f, path, seen = stack.pop()
            if len(path) == n:
                return path + [f]
            # if the graph top's values are multiple
            # lexical order's formal one is nearer from end and
            # we use stack => later one lexically formal one => we can return instantly,
            # if length is right
            for i in revIdMap[f]:
                if i not in seen:
                    stack.append([revLexTickets[i][1], path + [f], seen + [i]])
        return

        # looks same logic. diffrence is usign queue and usign stack

    # even access number looks same
    # the only thing is stack use "pop()" and queue use "pop(0)"
    # In Python pop() => O(1), pop(k) => O(k) => 1 > 0 but... I think something was set like that
    # This using stack time limit exceeds
    def findItinerary(self, tickets):
        n = len(tickets)
        lexTickets = sorted(tickets)
        idMap = collections.defaultdict(list)
        for i, (d, a) in enumerate(lexTickets):
            idMap[d].append(i)

        queue = [["JFK", [], []]]
        while queue:
            f, path, seen = queue.pop(0)
            if len(path) == n:
                return path + [f]

            for i in idMap[f]:
                if i not in seen:
                    queue.append([lexTickets[i][1], path + [f], seen + [i]])

        return

    def findItinerary(self, tickets):
        n = len(tickets)
        revLexTickets = sorted(tickets)[::-1]
        revIdMap = collections.defaultdict(list)
        for i, (d, a) in enumerate(revLexTickets):
            revIdMap[d].append(i)

        stack = [("JFK", [], [])]
        while stack:
            f, path, seen = stack.pop()
            if len(path) == n:
                return path + [f]
            for i in revIdMap[f]:
                if i not in seen:
                    stack.append((revLexTickets[i][1], path + [f], seen + [i]))
        return


S = Solution()
input = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
test = S.findItinerary(input)
print(test)
