"""
953. Verifying an Alien Dictionary
Easy

Share
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dictionary = {order[i]: i for i in range(len(order))}
        numerized = []
        for i in words:
            i = list(i)
            print(i, words)
            for k, v in enumerate(i):
                i[k] = dictionary[v]
            numerized.append(i)
        print(1, numerized)
        return all(w1 <= w2 for w1, w2 in zip(numerized, numerized[1:]))

        # 이전까지는 길지만 일단 오케이
        # pairs = zip(*numerized)
        # # print([pair for pair in pairs ])
        #
        # for j in pairs:
        #     for i in range(1, len(j)):
        #         if j[i - 1] > j[i]:
        #             return False
        # return True

    def isAlienSorted(self, words, order):
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        # zip이 원래 pair가 안맞으면 자동 잘리는걸 이용해서 zip(words, words[1:]) 이것으로 (,2), (2,3) 이런식의 pairs를 만든 것이다.
        # 그리고 이렇게 앞뒤짝을 이렇게 통으로 비교 해준다. [0, 15, 15, 11, 4], [0, 15, 15]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))


words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"

S = Solution()
test = S.isAlienSorted(words, order)
print(test)



