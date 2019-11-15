"""
274. H-Index
Medium

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.


***how to get h index
Formally, if f is the function that corresponds to the number of citations for each publication, we compute the h-index
as follows. First we order the values of f from the largest to the lowest value. Then, we look for the last position
in which f is greater than or equal to the position (we call h this position). For example, if we have a researcher
with 5 publications A, B, C, D, and E with 10, 8, 5, 4, and 3 citations, respectively, the h-index is equal to 4 because
the 4th publication has 4 citations and the 5th has only 3. In contrast, if the same publications have 25, 8, 5, 3, and
3 citations, then the index is 3 because the fourth paper has only 3 citations.
f(A)=10, f(B)=8, f(C)=5, f(D)=4, f(E)=3　→ h-index=4
f(A)=25, f(B)=8, f(C)=5, f(D)=3, f(E)=3　→ h-index=3


 h-index 산출 방법
1. 해당 연구자의 발표 논문을 피인용횟수가 많은 순으로 정렬합니다. 피인용횟수가 높은 순으로 번호를 부여합니다.
2. 논문의 번호(No)와 피인용횟수를 비교하여 피인용횟수가 논문의 번호(No)와 같거나 큰 번호(No)가 연구자의 h-index가 됩니다.
3. 위 예에서 번호(No)보다 피인용횟수가 낮아지는 6순위 바로 위의 5순위가 h-index가 됩니다.
4. 이 값의 의미는, 해당 저자가 발표한 논문 중 5개의 논문이 적어도 각 5번 인용되었다는 의미입니다.

**
in the example above index start from 1
**
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        result = 0
        sorted = self.quickSort(citations)
        for i, v in enumerate(sorted, 1):
            if v >= i:
                result = i
        return result

    def quickSort(self, nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[-1]
        l = []
        m = [nums[-1]]
        r = []
        for i in nums[:-1]:
            if i > pivot:
                l.append(i)
            elif i < pivot:
                r.append(i)
            else:
                m.append(i)

        left = self.quickSort(l)
        right = self.quickSort(r)

        return left + m + right

    def hIndex2(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        result = 0
        citations.sort(reverse=True)
        for i, v in enumerate(citations, 1):
            if v >= i:
                # because actual index starts from 0 in python list
                result = i
        return result


citations1 = [3,0,6,1,5] # =>3
citations = [] # =>1
s = Solution()
test = s.hIndex(citations1)
print(test)





























