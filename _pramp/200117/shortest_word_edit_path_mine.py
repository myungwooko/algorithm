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


# BFS
# Time complexity: O(n^2*k): n is for length of words, k is for length of a word.
# Space complexity: O(n*a): n is for length of words for queue, a is for the queue element.
# => a = ( n * 3 * average length of seen )
def shortestWordEditPath(source, target, words):
    queue = [(source, [], 0)]
    while queue:
        curr, seen, count = queue.pop(0)
        if curr == target:
            return count
        for word in words:
            if word != curr and (word not in seen):
                inner_count = 0
                for i in range(len(word)):
                    if word[i] != curr[i]:
                        inner_count += 1
                if inner_count == 1:
                    queue.append((word, seen + [curr], count + 1))
    return -1


source = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

test = shortestWordEditPath(source, target, words)
print(test)
