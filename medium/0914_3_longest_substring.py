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


def lengthOfLongestSubstring(s: str) -> int:
    """
    - 문제를 차분히 잘 확인하고 이해해야한다. 요지를 분명히 파악하라.
    ex) "abcabv" 두번째 a 나왔으니 앞에 다 끊고 두번쨰 a 부터 새로 시작하면 되는게 아니라 첫번째 a만 잘라내고 유효하게 카운팅해서 비교해 나가면 된다.
         문제의 요지는 연결된 중복된 글자를 갖지 않는 글자들의 조합중 가장 긴것을 찾는 것.
    - 예외처리 및 모든 경우의 수에 대해서 생각해야 한다.
    - 위의 과정을 면접관과의 커뮤니케이션으로 분명히 해야한다.
    - test case 를 내가 작성해야 한다.

    """
    if len(s) <= 1:
        return len(s)
    map = {s[0]: 1}
    sub = s[0]
    for i, v in enumerate(s[1:]):
        if v in sub:
            map[sub] = len(sub)
            index = sub.find(v)
            sub = sub[index + 1:] + v
        else:
            sub += v
            if i is len(s[1:]) - 1:
                map[sub] = len(sub)
    return max(list(map.values()))


test1 = lengthOfLongestSubstring("pwwkew")
print('expected is 3', test1)
test2 = lengthOfLongestSubstring("au")
print('expected is 2', test2)
test3 = lengthOfLongestSubstring("abcabv")
print('expected is 4', test3)
