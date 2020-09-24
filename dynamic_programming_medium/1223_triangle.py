"""
120. Triangle
Medium

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


바로 다음 단계에서 가장 작은걸로 간다고 그게 총 움직임에서 최소가 되라는 법은 없다.
과정중 음수가 존재할 수 있기 떄문
so 바로 아래에서는 큰쪽으로 간다해도 최종적으로는 최소값이 되는 것이 나올 가능성이 있는 구조.
"""


class Solution(object):
    ## recursive
    #     def minimumTotal(self, triangle):
    #         if not triangle:
    #             return
    #         if len(triangle) == 1:
    #             return triangle[0][0]
    #         res = []

    #         def helper(r, c, sum):
    #             if r == len(triangle):
    #                 if not res:
    #                     res.append(sum)
    #                 else:
    #                     if sum < res[0]:
    #                         res[0] = sum
    #                 return
    #             helper(r+1, c, sum+triangle[r][c])
    #             helper(r+1, c+1, sum+triangle[r][c+1])
    #             return
    #         helper(1, 0, triangle[0][0])
    #         return res[0]

    # bottom-up, O(n) space
    def minimumTotal(self, triangle):
        if not triangle:
            return
        res = triangle[-1]
        print(1, res)
        # from index right before last to 0
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # only one element is changed and the one thing will not used at the next comparing turn.
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]


input = [[-1], [2, 3], [1, -1, -3]]
input2 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
input3 = [[2], [3, 4], [6, 5, 7], [4, 1, 6, 3], [5, 7, 6, 4, 2]]
input4 = [[2], [3, 4], [6, -5, 1], [4, 1, 8, -8], [5, 7, 6, 4, 1]]
"""
We can check it works properly through using input4 as an argument.
- top down => just selecting smaller one from selectable next row's two is not working 
- bottom up => is working 
*Those two are totally different because top down is just for one case and bottom up is for every cases.
*recursive version for top down is working but is uses a lot of time.
"""
s = Solution()
test = s.minimumTotal(input4)
print(test)
