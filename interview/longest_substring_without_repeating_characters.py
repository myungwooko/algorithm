"""
3. Longest Substring Without Repeating Characters
Medium

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
length 구하는 것
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        map = {s[0]: 1}
        sub = s[0]
        for i, v in enumerate(s[1:]):
            if v in sub:
                map[sub] = len(sub)
                index = sub.find(v)
                #앞의 것은 카운트 했으니 오히려 앞의 중복 요소를 제외하고 현재것(중복기준 뒤)의 기준으로 기본 가장 긴것을 만들어주는 과정. 그리고 거기서 부터 진행
                sub = sub[index + 1:] + v
            else:
                sub += v
                if i is len(s[1:])-1:
                    map[sub] = len(sub)
        return max(map.values())

S = Solution()
s = "abcabcbb"
test = S.lengthOfLongestSubstring(s)
print(test)

"""
substring 자체를 구하는 
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return 1
        d = {s[1]: 1}
        sub = s[1]
        for i in range(1, len(s)):
            if s[i] in sub:
                d[sub] = len(sub)
                index = sub.find(s[i])
                sub = sub[index+1:] + s[i]
            else:
                sub += s[i]
                if i == len(s) - 1:
                    d[sub] = len(sub)
        result = ""
        for k in d:
            if not result:
                result = k
            else:
                if len(k) > len(result):
                    result = k
        return result

S = Solution()
s = "abcabcbb"
test = S.lengthOfLongestSubstring(s)
print(test)