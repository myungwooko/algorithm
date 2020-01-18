"""
344. Reverse String
Easy

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n - 1, -1, -1):
            char = s.pop(i)
            s.append(char)
        return s

    # case => not in-place
    # def reverseString(self, s):
    #     """
    #     :type s: List[str]
    #     :rtype: None Do not return anything, modify s in-place instead.
    #     """
    #     return s[::-1]

