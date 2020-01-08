"""
242. Valid Anagram
Easy

1042

126

Add to List

Share
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1, dic2 = {}, {}
        for i in s:
            dic1[i] = dic1.get(i, 0) + 1
        for j in t:
            dic2[j] = dic2.get(j, 0) + 1
        return dic1 == dic2

    # def isAnagram(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     return sorted(s) == sorted(t)

