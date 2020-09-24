"""
1268. Search Suggestions System
Medium

Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names
from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.



Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]


Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
"""


class Solution:
    # brute force
    #     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    #         if not products or not searchWord:
    #             return []
    #         result = []
    #         part = ""
    #         for i in searchWord:
    #             part += i
    #             result.append(self.makingCandidates(part, products))
    #         return result

    #     def makingCandidates(self, part, products):
    #         e = len(part)
    #         return sorted([w for w in products if w[:e] == part])[:3]
    """
    Trie: 한단계 한단계 유효한 것에 대한 후보군을 모두 child로 가지고 있는 구
    """
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        trie = {"words": []}

        def helper(t, word, depth):
            if word[depth:] == "":
                return
            idx = word[depth]
            if idx not in t:
                t[idx] = {"words": []}
            t[idx]["words"].append(word)
            helper(t[idx], word, depth + 1)

        for word in products:
            helper(trie, word, 0)

        # print(90, trie)
        """
        trie
        
         products = ["mobile","moneypot","monitor","mouse","mousepad"]
         {'words': [], 
            'm': {'words': ['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 조
                    # m에 대해 유효한것 -> 안으로 들어와서 mo가 되는 것들에 대한 후보를 가지고 있는 개념, 밑의 같은 구조는 그런식으로 이해하면 된다. 
                    'o': {'words': ['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'],
                            'b': {'words': ['mobile'], 
                                    'i': {'words': ['mobile'], 
                                            'l': {'words': ['mobile'], 
                                                    'e': {'words': ['mobile']}}}}, 
                            'u': {'words': ['mouse', 'mousepad'], 
                                's': {'words': ['mouse', 'mousepad'], 
                                    'e': {'words': ['mouse', 'mousepad'], 
                                        'p': {'words': ['mousepad'], 
                                            'a': {'words': ['mousepad'], 
                                                'd': {'words': ['mousepad']}}}}}}, 
                            'n': {'words': ['moneypot', 'monitor'], 
                                'e': {'words': ['moneypot'],
                                    'y': {'words': ['moneypot'], 
                                        'p': {'words': ['moneypot'], 
                                            'o': {'words': ['moneypot'], 
                                                't': {'words': ['moneypot']}}}}}, 
                                'i': {'words': ['monitor'], 
                                    't': {'words': ['monitor'], 
                                        'o': {'words': ['monitor'], 
                                            'r': {'words': ['monitor']}}}}}}}}
        """
        res = []
        for i, char in enumerate(searchWord):
            if not trie or char not in trie:
                res += [[]] * (len(searchWord) - i)
                break
            res.append(sorted(trie[char]["words"])[:3])
            trie = trie[char]

        return res


s = Solution()
p = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
word = "mouse"
test = s.suggestedProducts(p, word)
print(test == [["mobile", "moneypot", "monitor"],
               ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"],
               ["mouse", "mousepad"], ["mouse", "mousepad"]])
