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


# BFS
# Time Complexity:
# O(n^2*k) n is total number of all possible elements of queue and which is also length of words, k is length of a word
# Space Complexity: O(n) for queue, n is as same as Time Complexity's
def shortestWordEditPath(source, target, words):
    queue = [(source, [source], 0)]
    while queue:
        curr, seen, count = queue.pop(0)
        if curr == target:
            return count
        for word in words:
            if word not in seen:
                diff = 0
                for i in range(len(word)):
                    if curr[i] != word[i]:
                        diff += 1
                if diff == 1:
                    queue.append([word, seen + [word], count + 1])
    return -1


# DFS
# Time Complexity: O(n^2*k), but exponential
# Space Complexity: O(n) for res
def shortestWordEditPath(source, target, words):
    res = []

    def helper(current, seen, count):
        if current == target:
            res.append(count)
            return

        for word in words:
            if word not in seen:
                diff_char = 0
                for i in range(len(word)):
                    if word[i] != current[i]:
                        diff_char += 1
                if diff_char == 1:
                    helper(word, seen + [current], count + 1)

    helper(source, [source], 0)
    return min(res) if res else -1


source = "hit"
target = "cog"
words = ["hot","dot","dog","lot","log","cog"]

test = shortestWordEditPath(source, target, words)
print(test)
