"""
767. Reorganize String
Medium

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
from collections import Counter
from heapq import heappush, heappop


#많은 것부터 먼저 해결해야 나중에 남는일이 안생긴다. 기본적으론 그러한 조건으로 다른글자를 갖다붙이는 논리.
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        max_freq = Counter(S).most_common(1)[0][1]
        print(Counter(S), Counter(S).most_common(2))
        #  if (2 * max_freq) - 1 is bigger than total length, it can't be right. because total length should be at least 2*(max+freq) - 1 so that contain max freq element separated.
        if (2 * max_freq) - 1 > len(S):
            return ""
        else:
            heap = []
            # -를 붙이는 이유는 큰게 앞으로 오도록. => add - is meaning most frequent one can be most front position in the heap.
            for k,v in Counter(S).items():
                heappush(heap, (v*-1, k))
            print(heap)
            result = []
            while heap:
                v,k = heappop(heap)
                if not result or k != result[-1]: # can add the top most element
                    result.append(k)
                    if v != -1:
                        # decrease number of freq
                        heappush(heap,(v+1,k))
                else:                             # cannot add the top most element
                    v1, k1 = heappop(heap)
                    #Counter object로 만들면서 분류했으므로 절대 같을수는 없는 것이
                    result.append(k1)
                    heappush(heap, (v,k))
                    if v1 != -1:
                        heappush(heap, (v1+1,k1))
                        print(1, heap)
                    print(2, heap)
            return "".join(result)

S = "aab"
s = Solution()
test = s.reorganizeString(S)
print(test)