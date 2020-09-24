"""
802. Find Eventual Safe States
Medium

In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.
If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.
More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.
The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

Illustration of graph

Note:

graph will have length at most 10000.
The number of edges in the graph will not exceed 32000.
Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].
"""


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """


"""
discuss

#1
The idea is to just use plain DFS with a state = {Initial=0, InProgress=1, Completed=2 }.
When traversing through the graph, if we detect a cycle by encountering a node which is InProgress
if visited[node] == 1
OR
by visiting a node that is already part of a cycle
node in cycle
these two imply that the path we have constructed/traversed so far, all the nodes in the path, are connected to a cycle, so we add them to the cycle set()

cycle |= set(path)

    def eventualSafeNodes(self, graph):
        def dfs(node, path, visited, cycle):
            if visited[node] == 1 or node in cycle:
                cycle |= set(path)
            elif visited[node] == 0:
                path.append(node)
                visited[node] = 1
                for child in graph[node]:
                    dfs(child, path, visited, cycle)
                visited[node] = 2
                path.pop()

        cycle, visited = set(), [0] * len(graph)
        for node in range(len(graph)):
            dfs(node, [], visited, cycle)
        return sorted(set(range(len(graph))) - cycle)
"""
