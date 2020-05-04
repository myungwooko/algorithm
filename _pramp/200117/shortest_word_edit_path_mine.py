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
    results = []
    if len(source) != len(target):
        return -1
    results = []

    def helper(curr, seen, count):
        if curr == target:
            results.append(count)
            return

        candidates = []
        for word in words:
            if len(curr) != len(word):
                continue

            diff = 0
            for i in range(len(curr)):
                if curr[i] != word[i]:
                    diff += 1

            if diff == 1:
                candidates.append(word)

        if not candidates:
            return

        for candi in candidates:
            if candi in seen:
                continue
            helper(candi, seen + [curr], count+1)  # recursion에서 reference를 끊기 위해 새로 생성되는 새로운 주소값을 넣기 위해서 이렇게 해준다.
        return

    helper(source, [], 0) # 그래서 set이 아닌 list를 썼다. set은 add로 넣게 되면 같은 주소값 같은 set 오브젝트를 참조하니까.
    if results:
        return min(results)
    return -1


# queue
# Time: O(N*M) / N is length of words and M is length of a word(source or target)
# => 이것은 결국 최대 모든 node(여기서 node는 queue에 대한 모든 가능한 element를 말함 *(source, seen, count))
def shortestWordEditPath(source, target, words):
    queue = [(source, [])]

    while queue:
        curr, seen = queue.pop(0)
        if curr == target:
            return len(seen)

        for word in words:
            idx = count = 0
            while idx < len(word):
                if word[idx] != curr[idx]:
                    count += 1
                idx += 1
            if word not in seen and count == 1:
                queue.append((word, seen + [word]))
    return -1


def shortestWordEditPath(source, target, words):
    queue = [(source, [], 0)]
    while queue:
        curr, seen, count = queue.pop(0)
        if curr == target:
            return count
        for word in words:
            diff = 0
            if word not in seen and word != curr:
                for i in range(len(word)):
                    if curr[i] != word[i]:
                        diff += 1
                if diff == 1:
                    queue.append((word, seen + [curr], count + 1))
    return -1

source = "hit"
target = "cog"
words = ["hot","dot","dog","lot","log","cog"]

test = shortestWordEditPath(source, target, words)
print(test)