"""
969. Pancake Sorting
Medium

224

275

Favorite

Share
Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then "reverse" the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

Example 1:
Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.
Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.

Note:

1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]

mine
- the biggest one has to go to the end
- then we can reduce the size of object we has to sort.
"""


class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        while len(A) > 0:
            maxVal = max(A)
            idxMax = A.index(maxVal)
            if idxMax != 0:
                res.append(idxMax + 1)
                tmp = A[:idxMax + 1]
                tmpRvs = tmp[::-1]
                preA = tmpRvs + A[idxMax + 1:]
                preA = preA[::-1]
                res.append(len(preA))
                A = preA[:-1]
            else:
                A = A[::-1]
                res.append(len(A))
                A = A[:-1]
            if len(A) == 1:
                break
        return res


input = [3, 2, 4, 1]
s = Solution()
test = s.pancakeSort(input)
print(test)
