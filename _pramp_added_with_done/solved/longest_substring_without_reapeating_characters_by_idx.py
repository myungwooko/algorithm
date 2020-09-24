"""
Longest Substring Without Repeating Characters by index

Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: (0, 2)
Explanation: The answer is (0, 2), with the range of index of "abc".

Example 2:
Input: "bbbbb"
Output: 0
Explanation: The answer is 0,  with the first index of "b".

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is (2, 4), with the range of "wke".
"""


# brute force
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        if not s:
            return
        result = (0, 0)
        for i in range(len(s)):
            seen = set()
            seen.add(s[i])
            for j in range(i + 1, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                else:
                    # j-1 => because this turn is repeated turn and we want to check non repeated arrange valid one
                    if result[1] - result[0] < (j - 1) - i:
                        result = (i, j - 1)
                    break
        if result[0] == result[1]:
            return result[0]
        return result


S = Solution()
test1 = S.lengthOfLongestSubstring("abcabcbb")
print(test1, test1 == (0, 2))
test2 = S.lengthOfLongestSubstring("bbbbb")
print(test2, test2 == 0)
test3 = S.lengthOfLongestSubstring("pwwkew")
print(test3 == (2, 4))
test4 = S.lengthOfLongestSubstring("b")
print(test4 == 0)
