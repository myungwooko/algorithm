"""
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least
h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
             received 0, 1, 3, 5, 6 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        """
        mid 인데스로 탐색 마지막이 인덱스를 1로서 가정하고 1씩 더해나가는 개념이라고 상정하면
        mid를 구하면 해당 mid의 인덱스는 => (마지막 인덱스 - 해당 mid 인덱스 + 1)
        mid => 자신은 h 인덱스를 만족시키고 그 다음것은 h인덱스를 만족시키지 못하는 거나 그게 일반 인덱스 기준 0이면 그것의
        계산된 h index가 답이 된다.

        use binary search using mid index.
        assume last index is index 1(as applied h index)
        assume actual -1 index from last as a added 1 index in each step as follow h_index concept.
        actual mid index => index followed h index concept = last index - actual mid index
        if mid satisfies h_index before mid is not or mid's actual index is 0
        return the h_index
        till search every element or return => binary search in that logic
        if it is returned, that's it or return 0
        """
        if not citations:
            return 0
        l, r = 0, len(citations) - 1
        while l <= r:
            mid = l + (r - l) // 2
            hIndex = len(citations) - mid
            beforeH = len(citations) - (mid - 1)
            if hIndex <= citations[mid]:
                if beforeH > citations[mid - 1] or mid == 0:
                    return hIndex
                else:
                    r = mid - 1
            else:
                l = mid + 1
        return 0

    # simpler
    """
    - if there is no h index => will go to last index then lastly  l = mid + 1 will be excuted => n-l = 0
    - if every elements are satisfied as h index lastly l will be 0 as it was at the first time => n-l = n
    so these cases are handled in the below logic naturally.  
    """
    def hIndex(self, citations):
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)/2
            if citations[mid] >= n-mid:
                r = mid - 1
            else:
                #마지막에(해당 자신들이 같아지는 포인트에서) 자기 자신이 만족시키지 못하면 자기 자신에서 +1을 하는데 그것은 현재의 r이 이전의 mid에서 만족이 되고 넘어오기 전의 그 위치이기 때문에
                #마지막에 +1을 하면 마지막 기준을 충족하던 것으로 가는 것이된다. 그래서 우리는 l을 기준으로 return 값을 계산하게 되는 것.
                l = mid + 1
        return n-l

