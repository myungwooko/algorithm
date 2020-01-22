"""
139. Word Break
Medium

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false


referenced from: https://leetcode.com/problems/word-break/discuss/164472/Python-solution
"""
class Solution(object):
    """
    dp solution
    """
    def wordBreak(self, s, wordDict):
        # 해당 인덱스의 앞까지가 segment로서 해당 부분까지를 완성시키는가에 대한 dp
        dp = [False] * (len(s) + 1)
        dp[0] = True
        # i = dp index
        for i in range(1, len(s) + 1):
            # 기준에 대한 segment를 만들기 위함
            for j in range(i):
                seg = s[j:i]
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        # 결국 축적하면서 우리가 알고싶었던건 마지막 =>즉, 전체가 다 segment 되는가? 이다.
        return dp[-1]

    """
    The above algorithm can also be implemented in a top-down fashion, as below. The time complexity   
    and space complexity is the same as above.
    Dynamic Programming top down (memoization) 
    """
#     def wordBreak(self, s, wordDict):
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """

#         def dfs(i):
#             if i == len(s):
#                 return True
#             if rec[i] != -1:
#                 return True if rec[i] == 1 else False
#             for j in range(i, len(s)):
#                 if s[i:j + 1] in wordSet:
#                     rec[j + 1] = 1 if dfs(j + 1) else 0
#                     if rec[j + 1] == 1:
#                         return True
#             return False

#         rec = [-1] * (len(s) + 1)
#         wordSet = set(wordDict)
#         return dfs(0)

#     #recursion time limit exceeds
#     def wordBreak(self, s, wordDict):
#         result = []
#         def recursion(s):
#             if not s:
#                 return True
#             part = ""
#             for i in range(len(s)):
#                 part += s[i]
#                 if part in wordDict:
#                     result.append(recursion(s[i+1:]))
#             return False
#         recursion(s)
#         return any(result)


string = "cars"
wordDict = ["car", "ca", "rs"]
s = Solution()
test = s.wordBreak(string, wordDict)
print(test)