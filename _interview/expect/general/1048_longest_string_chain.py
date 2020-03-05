"""
1048. Longest String Chain
Medium

528

40

Add to List

Share
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.
For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.



Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".


Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
"""
class Solution:
    def longestStrChain(self, words):
        words.sort(key=lambda x: len(x))
        cLs = []
        paths = []

        def helper(idx, path, chainLength):
            candidates = []
            for i in range(idx + 1, len(words)):
                if len(words[idx]) + 1 == len(words[i]) and self.successor(words[idx], words[i]):
                    candidates.append((i, path + [words[i]], chainLength + 1))

            if not candidates:
                cLs.append(chainLength + 1)
                paths.append((path, chainLength + 1))
                return

            for j, path, cL in candidates:
                helper(j, path, cL)

        for i in range(len(words)):
            helper(i, [words[i]], 0)

        return max(cLs)

    def successor(self, word1, word2):
        count = 0
        diffCount = 0

        l = r = 0
        while l < len(word1):
            if word1[l] != word2[r]:
                diffCount += 1

                if diffCount > 1:
                    return False
                count += 1
                r += 1
            else:
                l += 1
                r += 1

        if count == 1 or r == len(word2) - 1:
            return True
        return False

    # DP
    """
    Explanation
    - Sort the words by word's length. (also can apply bucket sort)
    - For each word, loop on all possible previous word with 1 letter missing.
    - If we have seen this previous word, update the longest chain for the current word.
    - Finally return the longest word chain.

    Complexity
    Time O(NlogN) for sorting,
    Time O(NSS) for the for loop, where the second S refers to the string generation and S <= 16.
    Space O(NS)
    """
    def longestStrChain(self, words):
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())


words1 = ["a","b","ba","bca","bda","bdca"]
words2 = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
S = Solution()
test1 = S.longestStrChain(words1)
test2 = S.longestStrChain(words2)
print(1, test1)
print(2, test2)



