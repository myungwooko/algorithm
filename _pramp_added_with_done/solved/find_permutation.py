'''
Our profanity filter is responsible for blocking users’ messages that contain sensitive text. Recently,
one of our clients has been complaining about users sending permutations of sensitive texts, and would like to block the permutations as well.

Implement an algorithm that will find all permutations of string s in string t.
Return the results as a list of pairs, where each pair represents the start and end index of the permutation found.

Example:
Input
s = "secret" => any string that has the same character and character count values
t = "trceestor"
Output
[(0,5), (1,6)]
(0,5) Names the the string “trcees” which is a permutation of secret. (1,6) “rceest” is also a permutation of secret. However, even though the string “ceestor” contains all the letters in secret, it’s not quite a permutation so its not counted.
'''
import collections


def findPermutation(s, t):
    compared = collections.Counter(s)
    l = len(s)
    res = []
    acc = 0
    for i, v in enumerate(t):
        if v in compared:
            compared[v] -= 1

        # values() alsoO(N), N is number of key of compared
        if acc == l - 1 and (len(set(compared.values())) == 1
                             and list(compared.values())[0] == 0):
            res.append((i, i - l + 1))
            acc -= 1
            compared[t[i - l + 1]] += 1
        acc += 1
    return res


test = findPermutation("secret", "trceestor")
print(test)


def findPermutation(s, t):
    compared = collections.Counter(s)
    l = len(s)
    res = []
    dic = {}
    for i, v in enumerate(t):
        if i >= l:
            dic[t[i - l]] -= 1
        if not dic.get(v, None):
            dic[v] = 1
        else:
            dic[v] += 1

        # another time complexity O(N), N is number of key of dic
        if dic == compared:
            res.append((i, i - l + 1))

    return res


test = findPermutation("secret", "trceestor")
print(test)
