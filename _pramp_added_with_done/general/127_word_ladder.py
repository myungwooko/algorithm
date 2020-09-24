"""
127. Word Ladder
Medium

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""


class Solution:
    # dfs
    def ladderLength(self, source, target, words):
        """
        @param source: str
        @param target: str
        @param words: str[]
        @return: int
        """
        results = []
        if len(source) != len(target):
            return -1

        def helper(word, seen, count):
            if word == target:  # is 보단 ==
                results.append(count)
            candidates = []
            for i in range(len(words)):
                wordComp = words[i]
                cc = 0
                for j in range(len(word)):
                    if word[j] != wordComp[j]:
                        cc += 1
                if cc == 1:
                    candidates.append(words[i])
            if not candidates:
                return

            for k in candidates:
                if k in seen:
                    continue
                helper(
                    k, seen + [word], count + 1
                )  ############################ """recursion에서 reference를 끊기 위해 새로 생성되는 새로운 주소값을 넣기 위해서 이렇게 해준다."""
            return -1

        helper(
            source, [], 0
        )  ###########################   그래서 set이 아닌 list를 썼다. set은 add로 넣게 되면 같은 주소값 같은 set 오브젝트를 참조하니까.
        if results:
            return min(results) + 1
        else:
            return -1

    # 다 만들어본뒤 비교하는 알고리즘. 같은 레벨이기때문에 처음 타겟을 만났을떄 리턴하면 그걸로 된다. 아니면 끝까지 다해보고 없으면 0 리턴.
    #bfs queue
    def ladderLength(self, beginWord, endWord, wordList):
        queue = [(beginWord, 1)]
        visited = set()

        while queue:
            word, dist = queue.pop(0)
            if word == endWord:
                return dist
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + j + word[i + 1:]
                    if tmp not in visited and tmp in wordList:
                        queue.append((tmp, dist + 1))
                        visited.add(tmp)
        return 0


class Solution:
    """
    Bi-directional BFS
    
    Instead of two queues, we use two sets. We add start and stop to them and remove them from wordList. We call the sets src and sink.
    In every iteration of the loop we pick the set/queue with lesser number of values. In every iteration we progress one level towards destination.
    Note we do not filter using wordList in get_candidates. This is key to getting this algorithm right. Think about it why ? 
    We find a match when one of the candidates from say src is already in the set for sink. Since that candidate was added to sink 
    it must have been removed from wordList. Therefore if we filter with wordList while generating candidates, we can never expect to find a match in sink (other queue's set).
    """
    def get_candidates(self, word):
        word = [x for x in word]
        all_chars = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(word)):
            org = word[i]
            for ch in all_chars:
                if ch != org:
                    word[i] = ch
                    yield "".join(word)
                    word[i] = org

    def ladderLength(self, start, stop, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: list[str]
        :rtype: int
        """
        src, sink, wordList = set([start]), set([stop]), set(wordList)
        if start in wordList:
            wordList.remove(start)
        if stop in wordList:
            wordList.remove(stop)
        else:
            return 0
        d = 0
        while len(src) != 0 and len(sink) != 0:
            d, new_set = d + 1, set([])
            if len(src) > len(sink):  # Pick the smaller queue
                src, sink = sink, src
            for wd in src:
                for c in self.get_candidates(wd):
                    if c in sink:
                        return d + 1
                    elif c in wordList:
                        new_set.add(c)
                        wordList.remove(c)
            src = new_set
        return 0


s = Solution()
source = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

# source = "bit"
# target = "pog"
# words = ["but","put","big","pot","pog","pig","dog","lot"]
# bit => but => put => pot => pog
#                   => pot => pog

# bit => big => pig => pog

test = s.wordLadder(source, target, words)
print(test)
