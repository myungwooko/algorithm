"""
207. Course Schedule
Medium

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """


"""
discuss

#1
# BFS: from the end to the front
def canFinish1(self, numCourses, prerequisites):
    forward = {i: set() for i in xrange(numCourses)}
    backward = collections.defaultdict(set)
    for i, j in prerequisites:
        forward[i].add(j)
        backward[j].add(i)
    queue = collections.deque([node for node in forward if len(forward[node]) == 0])
    while queue:
        node = queue.popleft()
        for neigh in backward[node]:
            forward[neigh].remove(node)
            if len(forward[neigh]) == 0:
                queue.append(neigh)
        forward.pop(node)
    return not forward  # if there is cycle, forward won't be None

# BFS: from the front to the end    
def canFinish2(self, numCourses, prerequisites):
    forward = {i: set() for i in xrange(numCourses)}
    backward = collections.defaultdict(set)
    for i, j in prerequisites:
        forward[i].add(j)
        backward[j].add(i)
    queue = collections.deque([node for node in xrange(numCourses) if not backward[node]])
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for neigh in forward[node]:
            backward[neigh].remove(node)
            if not backward[neigh]:
                queue.append(neigh)
    return count == numCourses
    
# DFS: from the end to the front
def canFinish3(self, numCourses, prerequisites):
    forward = {i: set() for i in xrange(numCourses)}
    backward = collections.defaultdict(set)
    for i, j in prerequisites:
        forward[i].add(j)
        backward[j].add(i)
    stack = [node for node in forward if len(forward[node]) == 0]
    while stack:
        node = stack.pop()
        for neigh in backward[node]:
            forward[neigh].remove(node)
            if len(forward[neigh]) == 0:
                stack.append(neigh)
        forward.pop(node)
    return not forward
        
# DFS: from the front to the end    
def canFinish(self, numCourses, prerequisites):
    forward = {i: set() for i in xrange(numCourses)}
    backward = collections.defaultdict(set)
    for i, j in prerequisites:
        forward[i].add(j)
        backward[j].add(i)
    stack = [node for node in xrange(numCourses) if not backward[node]]
    while stack:
        node = stack.pop()
        for neigh in forward[node]:
            backward[neigh].remove(node)
            if not backward[neigh]:
                stack.append(neigh)
        backward.pop(node)
    return not backward



#2
def canFinish(self, n, prerequisites):
    G = [[] for i in range(n)]
    degree = [0] * n
    for j, i in prerequisites:
        G[i].append(j)
        degree[j] += 1
    bfs = [i for i in range(n) if degree[i] == 0]
    for i in bfs:
        for j in G[i]:
            degree[j] -= 1
            if degree[j] == 0:
                bfs.append(j)
    return len(bfs) == n

"""