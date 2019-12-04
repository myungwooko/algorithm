"""
406. Queue Reconstruction by Height
Medium

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


We first sort the list people, in the order of descending height. If multiple people are of the same height, sort them in
ascending order of the number of people in front of them. For example, if people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
after the line people_sorted = sorted(people, key = lambda x: (-x[0],x[1])), people_sorted = [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]].
Then for each person [i,j], their index in people_sorted is larger than or equal to j (due to the way we sort people).
Hence to obtain the final results, we just need to construct an empty list res, and starting from the left,
insert each element [i,j] in people_sorted to position j in res (Latter insertions of [i',j'] won't affect j
because either i' < i, or i' == i and j' > j). The time complexity of the algorithm is O(n^2): We loop over people once,
and each insertion is an O(n) operation. The space complexity is O(n).

We illustrate the above procedure with people_sorted, as i goes from 0 to 5, the empty list res changes as follows:

[[7,0]] (insert [7,0] at index 0)
[[7,0],[7,1]] (insert [7,1] at index 1)
[[7,0],[6,1],[7,1]] (insert [6,1] at index 1)
[[5,0],[7,0],[6,1],[7,1]] (insert [5,0] at index 0)
[[5,0],[7,0],[5,2],[6,1],[7,1]] (insert [5,2] at index 2)
[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] (insert [4,4] at index 4)

큰애들 부터 자신의 인덱스 확보된 채로 넣는개념.
그럼 뒤에 애들은 자신보다 튼애들이 이미 끝난 상태에서 자신의 인덱스에 상응하는 큰애들을 딱 놓고, 인덱스를 찾아서 넣기만 하면 되는 개념.
"""
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        print('after sorting', people)
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
s = Solution()
test = s.reconstructQueue(input)
print(test)

