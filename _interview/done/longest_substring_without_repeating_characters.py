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
=> 생각해보니 dic를 만들필요없이 그냥 list나 res string에 넣으면 될 것 같다. 
"""
# Because of find Time O(n^2)
class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)

        dic = {s[0]: 1}
        sub = s[0]

        for i in range(1, len(s)):
            if s[i] in sub:
                idx = sub.index(s[i])
                dic[sub] = len(sub)
                # 앞의 것은 카운트 했으니 오히려 앞의 중복 요소를 제외하고 현재것(중복기준 뒤)의 기준으로 기본 가장 긴것을 만들어주는 과정. 그리고 거기서 부터 진행
                sub = sub[idx+1:] + s[i]
            else:
                sub += s[i]
                if i == len(s)-1:
                    dic[sub] = len(sub)
        return max(dic.values())


S = Solution()
s = "abcabcbb"
test = S.lengthOfLongestSubstring(s)
print(test)

"""
substring 자체를 구하는 
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        d = {s[0]: 1}
        sub = s[0]
        for i in range(1, len(s)):
            if s[i] in sub:
                d[sub] = len(sub)
                idx = sub.find(s[i])
                #앞의 것은 카운트 했으니 오히려 앞의 중복 요소를 제외하고 현재것(중복기준 뒤)의 기준으로 기본 가장 긴것을 만들어주는 과정. 그리고 거기서 부터 진행
                sub = sub[idx+1:] + s[i]
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

    # 굳이 dict를 사용할 필요는 없어 보인다. length를 구하는 것도 마찬가지로 보인다. <================================================================= 이런식으로 전부 가능!
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        sub = s[0]
        res = ""
        for i in range(1, len(s)):
            if s[i] in sub:
                if not res or len(res) < len(sub):
                    res = sub
                idx = sub.find(s[i])
                #앞의 것은 카운트 했으니 오히려 앞의 중복 요소를 제외하고 현재것(중복기준 뒤)의 기준으로 기본 가장 긴것을 만들어주는 과정. 그리고 거기서 부터 진행
                sub = sub[idx+1:] + s[i]
            else:
                sub += s[i]
                if i == len(s) - 1:
                    if not res or len(res) < len(sub):
                        res = sub
        return res


    # def lengthOfLongestSubstring(self, s):
    #     if len(s) <= 1:
    #         return len(s)
    #
    #     dic = {s[0]: 1}
    #     sub = s[0]
    #
    #     for i in range(1, len(s)):
    #         if s[i] in sub:
    #             idx = sub.index(s[i])
    #             dic[sub] = len(sub)
    #             # 앞의 것은 카운트 했으니 오히려 앞의 중복 요소를 제외하고 현재것(중복기준 뒤)의 기준으로 기본 가장 긴것을 만들어주는 과정. 그리고 거기서 부터 진행
    #             sub = sub[idx+1:] + s[i]
    #         else:
    #             sub += s[i]
    #             if i == len(s)-1:
    #                 dic[sub] = len(sub)
    #
    #     res = [(k, v) for k, v in dic.items()]
    #     res.sort(key= lambda x: (-x[1], x[0]))
    #     print(res)
    #     return res[0][0]

