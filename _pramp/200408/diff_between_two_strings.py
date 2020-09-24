"""
Diff Between Two Strings

Given two strings of uppercase letters source and target, list (in string form) a sequence of edits to convert from source
to target that uses the least edits possible.

For example, with strings source = "ABCDEFG", and target = "ABDFFGH"
we might return: ["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"]

More formally, for each character C in source, we will either write the token C, which does not count as an edit;
or write the token -C, which counts as an edit.

Additionally, between any token that we write, we may write +D where D is any letter, which counts as an edit.

At the end, when reading the tokens from left to right, and not including tokens prefixed with a minus-sign,
the letters should spell out target (when ignoring plus-signs.)

In the example, the answer of A B -C D -E F +F G +H has total number of edits 4 (the minimum possible), and ignoring subtraction-tokens,
spells out A, B, D, F, +F, G, +H which represents the string target.

If there are multiple answers, use the answer that favors removing from the source first.

Constraints:

[time limit] 5000ms

[input] string source
2 ≤ source.length ≤ 12

[input] string target
2 ≤ target.length ≤ 12

[output] array.string
"""


# https://leetcode.com/problems/edit-distance/
# Time O(2^(source.length + target.length))
# => Because it divided two ways everytime and then that will be divied two ways as well if the character is diffrent
# Excepting same character case, it will be divided two and it will increment only one index of one of two lists
# so worst case => every character diffrent and it will be divided two everytime and it will keep for almost every character for # two lists => That makes => Time O(2^(source.length + target.length))
def diffBetweenTwoStrings(source, target):
    def helper(i, j):
        path = []
        if i == len(source):
            while j < len(target):
                path.append("+" + target[j])
                j += 1
            return path
        elif j == len(target):
            while i < len(source):
                path.append("-" + source[i])
                i += 1
            return path

        if source[i] == target[j]:
            path = [source[i]] + helper(i + 1, j + 1)
        else:
            deleteCase = ["-" + source[i]] + helper(i + 1, j)
            addCase = ["+" + target[j]] + helper(i, j + 1)
            # If there are multiple answers, use the answer that favors removing from the source first.
            path = deleteCase if len(deleteCase) <= len(addCase) else addCase
        return path

    return helper(0, 0)


"""
source = "ABCDEFG"
             ^
target = "ABDFFGH"
             ^
path = [A, B, +"D"]

# visual of  O(2^(source.length + target.length)) 

        dfs(0, 0)                                                      1
    dfs(1, 0)                            dfs(0, 1)                     2
  dfs(2, 0) dfs(1, 1)                dfs(1, 1)    dfs(0, 2)            4
                                                                       8

                                                                       2^0 + 2^1....2^n = 2^(n + 1) - 1

                                                                       what is n?
                                                                       n = source.length + target.length

                                                                       delete everything from source
                                                                       add everything from target = source.length +                                                                            target.length
"""
"""
=========================================================================================Improved version of explanation

Visualized process how it goes =========================================================================================
check what is addcase and delete case and how it goes

source = "ABCDEFG"
i:          ^
target = "ABDFFGH"
j:          ^

path = [a, b, +d]

# 기준은 target characters에 대한 source로 부터의 path 완성. 
- same case   : path에 source[i] 넣고 => i+1, j+1
- add case    : j를 더한다. path에 +target[j] 해주고 => source와 target의 실제 index에 대한 실행의 의미로서 
=> i, j+1 *source[i]는 그대로 아직 비교대상으로서 머무르고, 필요글자 target[j]는 이미 더해줬으니 다음대상으로 넘어간다.
- delete case : i를 지운다. path에 -source[i] 해주고 => source와 target의 실제 index에 대한 실행의 의미로서 
=> i+1, j *source[i]는 지워졌으니 다음것 비교로 넘어가고, 그 비교대상은 아직 해결되지 않은 j   

========================================================================================================================
# * Time complexity => O(2^(m+n)) *m=len(source), n=len(target)
# 모두 다른 경우, 두개로 나뉘어지는 binary search의 과정이 m+n 층만큼 진행되므로.
# in the case of every characters are different, 
# we do binary search process(for dividing addCase and deleteCase) as much as m+n levels
# * Space complexity => O(n+m)
# if source and target are in total diffrent, delete all and add all and that use m+n
# 모두 다른 경우, 다 지우고 다 더하는 공간을 사용하므로.
"""


def diffBetweenTwoStrings(source, target):
    def helper(i, j):
        path = []
        if i == len(source):
            while j < len(target):
                path += ["+" + target[j]]
                j += 1
            return path
        if j == len(target):
            while i < len(source):
                path += ["-" + source[i]]
                i += 1
            return path

        if source[i] == target[j]:
            path = [source[i]] + helper(i + 1, j + 1)
        else:
            addCase = ["+" + target[j]] + helper(i, j + 1)
            deleteCase = ["-" + source[i]] + helper(i + 1, j)
            path = deleteCase if len(deleteCase) <= len(addCase) else addCase
        return path

    return helper(0, 0)
