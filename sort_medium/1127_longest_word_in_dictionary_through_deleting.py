"""
524. Longest Word in Dictionary through Deleting
Medium

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some
characters of the given string. If there are more than one possible results, return the longest word with the smallest
lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        result = ""
        for w in d:
            if len(w) > len(result) and self.passed(s, w):
                result = w
            elif len(w) == len(result):
                lexChecker = [result, w]
                lexChecker.sort()
                if lexChecker[0] == w and self.passed(s, w):
                    result = w
        return result

    def passed(self, s, w):
        for i in w:
            if i not in s:
                return False
        for i in s:
            if i not in w:
                s = s.replace(i, '', 1)
        preRes = ""
        wCopy = w
        for i in s:
            if i == wCopy[0]:
                preRes += i
                wCopy = wCopy[1:]
                if len(preRes) == len(w):
                    break
        if preRes == w:
            return True
        return False

    def findLongestWord2(self, s, d):
        def isSubsequence(x):
            print(1, x)
            it = iter(s)
            print(2, it, [i for i in it])
            return all(c in it for c in x)
        return max(sorted(filter(isSubsequence, d)) + [''], key=len)

ss = "abpcplea"
w = ["a","b","c"]
s = Solution()
test = s.findLongestWord(ss, w)
print(1, test)
