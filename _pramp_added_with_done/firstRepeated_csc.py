import collections


def firstMostRepeated(s):
    candidates = s.split(" ")
    candidates = [repeatedChecker(w, i) for i, w in enumerate(candidates)]
    results = sorted(candidates, key=lambda x: (-x[1], x[2]))
    if results[0][1] > 1:
        return results[0][0]
    return -1


def repeatedChecker(word, idx):
    m = collections.Counter(word)
    r = max(m.values())
    return (word, r, idx)


s = "helo r age"
s2 = "hello cic happy collectionc"
test = firstMostRepeated(s)
test2 = firstMostRepeated(s2)
print(test == -1)
print(test2 == "collectionc")