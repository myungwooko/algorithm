"""
Shortest Word Edit Path
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.

Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.

If the task is impossible, return -1.

Examples:

source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.
source = "no", target = "go"
words = ["to"]

output: -1
Constraints:

[time limit] 5000ms
[input] string source
1 ≤ source.length ≤ 20
[input] string target
1 ≤ target.length ≤ 20
[input] array.string words
1 ≤ words.length ≤ 20
[output] array.integer
"""
def shortestWordEditPath(source, target, words):
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
        if word == target: # is 보단 ==
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
            helper(k, seen + [word], count + 1) ############################ """recursion에서 reference를 끊기 위해 새로 생성되는 새로운 주소값을 넣기 위해서 이렇게 해준다."""
        return -1
    helper(source, [], 0)                      ###########################   그래서 set이 아닌 list를 썼다. set은 add로 넣게 되면 같은 주소값 같은 set 오브젝트를 참조하니까.
    if results:
        return min(results)
    else:
        return -1


source = "hit"
target = "cog"
words = ["hot","dot","dog","lot","log","cog"]

test = shortestWordEditPath(source, target, words)
print(test)