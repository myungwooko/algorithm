"""
692. Top K Frequent Words
Medium

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""
#not Python3 => Python
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # Time: O(n + klgk)
        # Space: O(n)
        from collections import Counter
        counter = Counter(words)
        freq = {}
        for w, f in counter.items():
            if f not in freq:
                freq[f] = []
            freq[f].append(w)
        res = []
        print(1, freq)
        for f in range(len(words), 0, -1):
            if f in freq:
                for w in freq[f]:
                    res.append((w, f))
            if len(res) >= k:
                break
        res.sort(cmp=lambda a,b: b[1]-a[1] if a[1] != b[1] else -1 if a[0] < b[0] else 1)
        return [i[0] for i in res[:k]]


word = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
s = Solution()
test = s.topKFrequent(word, k)
print(test = ["the", "is", "sunny", "day"])