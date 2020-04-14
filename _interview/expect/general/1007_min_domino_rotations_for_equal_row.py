"""
1007. Minimum Domino Rotations For Equal Row
Medium

414

132

Add to List

Share
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done_with_pramp, return -1.



Example 1:



Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.


Note:

1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000


Intuition
- Anyway, simply if it will be possible soluiton, one of the elements of A[0] and B[0] should exist in every pair of zip(A, B)
- if there is and we found it => just calculate this len(A)(<= because len(A) is len(B), it doesn't matter)) => so len(A)- max(A.count(x), B.count(x))
- because we are finding the smallest swapping count.

"""
class Solution:
    def minDominoRotations(self, A, B):
        for x in [A[0], B[0]]:
            if all(x in d for d in zip(A, B)):
                return len(A) - max(A.count(x), B.count(x))
        return -1


A = [2, 1, 2, 4, 2, 2]
B = [5, 2, 6, 2, 3, 2]
s = Solution()
test = s.minDominoRotations(A, B)
print(test)
