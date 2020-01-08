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
"""
    결국 정리하면
    1. prerequisite의 관계가 제대로 되려면 앞의 아무것도 없는 것이 있어야 한다.
    2. 최초의 앞에 아무것도 없는 것부터 찾아서 역추적하여 관계에 맞게 하나씩 지워 나가고 
    3. 지워나가는 과정에서 자연스럽게 자신의 앞이 없어진 것들은 앞의 것과 같이 자신의 앞의 것이 존재하지 않게 된 것으로서 queue에 넣어준다.
    => 그렇게 하나하나씩 체이닝의 과 
    4. 그렇게 없애다가서 forward가 비게 되면 noncyclic한 것으로서 찬명되고 그러면 True를 return 할수 있게 되고
    5. 무언가가 남아있으면 뭔가 redudancy가 있는 것이므로 return False를 하게 되면 되는것.
"""
import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        forward = {i: set() for i in range(numCourses)}
        backward = collections.defaultdict(set)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        # print(1, forward)
        # print(2, backward)
        # finding out the first one that has no prerequisite
        queue = collections.deque([node for node in forward if len(forward[node]) == 0])
        # print(3, queue)
        while queue:
            node = queue.popleft()
            # print(4, node)
            # 그로부터의 edge들
            for neigh in backward[node]:
                # 해당 edge확인 되면 삭제
                forward[neigh].remove(node)
                if len(forward[neigh]) == 0:
                    # 해당 것이 지워서 0이 되었다면 forward의 문법대로 이것 또한 자신의 prerequisite이 없다는 의미이므로 => 다시 그것을 위의 알고리즘으로 넣을 수 있는 조건을 충족시켰으므로 진행하기 위해 queue에 넣는다.
                    # 그리고 여기서 이게 한개가 아니라는 의미가 이게 성립안된다는 의미이다. 정말 심플하게는 하나의 강의를 듣기전에 바로 선행되어야 하는 과목은 단 하나만 있을수 있으므로.
                    queue.append(neigh)
                    # print(queue)
            # 아무것도 달려있지 않은 것으로 현재 진행하는 알고리즘의 대상이 되었었던거고, 이제 어쨌든 임무를 마무리했으니 key로서 마저도 삭제. 그리고 이것은 나중에 return 값을 구할떄에 forward를 체크하는데도 의미를 갖게 된다.
            forward.pop(node)
        return not forward  # if there is cycle, forward won't be None

s = Solution()
n, p = 2, [[1,0]]
test = s.canFinish(n, p)
print(test)
