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
    We first convert wordDict to a hashset wordSet to facilitate O(1) look-up. Next, we initialize an array of length
    len(s)+1, where

                            dp[i] denotes if s[:i] can be segmented into words in wordSet.

     We let dp[0] = 1, because the empty
    string can be segmented into words in wordSet (trivially). We iterate i over range(1, len(s)+1), and try to find the
    value for dp[i]. Now dp[i] = 1 if there is some 0 <= j < i, such that dp[j] == 1 and s[j:i] is in wordSet. Therefore,
     we iterate j in range(i), and check if such a j exists. If it does, we let dp[i] = 1, Otherwise, we let dp[i] = 0.
     Finally, we return dp[-1] == 1.

    Time complexity: O(n**3), where n = len(s), because there are two nested for loops, and the slicing s[j:i] costs an
    extra O(n). Space complexity: O(n).
    """
    def wordBreak(self, s, wordDict):
        # dp is about if s[:idx] is be able to be segmented of not
        dp = [False] * (len(s) + 1)
        # "" definetly segmented
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                # decreasing the extension, check that if the segment is in dict or not. and using dp, check before that part can be segmented or not
                # if both are true dp[i] = True
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        print(3, dp)
        return dp[-1]

    """
    The above algorithm can also be implemented in a top-down fashion, as below. The time complexity and space complexity 
    is the same as above.

    Dynamic Programming top down (memoization):
    """
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        def dfs(i):
            if i == len(s):
                return True
            if rec[i] != -1:
                return True if rec[i] == 1 else False
            for j in range(i, len(s)):
                if s[i:j + 1] in wordSet:
                    rec[j + 1] = 1 if dfs(j + 1) else 0
                    if rec[j + 1] == 1:
                        return True
            return False

        rec = [-1] * (len(s) + 1)
        wordSet = set(wordDict)
        return dfs(0)




string = "cars"
wordDict = ["car", "ca", "rs"]
s = Solution()
test = s.wordBreak(string, wordDict)
print(test)