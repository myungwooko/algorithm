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
#https://leetcode.com/problems/edit-distance/
# Time O(2^(source.length + target.length)) => Because it divided two ways everytime and then that will be divied two ways as well if the character is diffrent
# so except same character case it will be divided two and it will increment only one index of one of two lists
# so worst case => every character diffrent it will divided
def diffBetweenTwoStrings(source, target):
    def func(i, j):
        path = []
        if i == len(source):
            while j < len(target):
                path += ['+' + target[j]]
                j += 1
            return path
        elif j == len(target):
            while i < len(source):
                path += ['-' + source[i]]
                i += 1
            return path

        if source[i] == target[j]:
            path = [source[i]] + func(i + 1, j + 1)
        elif source[i] != target[j]:
            deleteCase = ["-" + source[i]] + func(i+1, j)
            addCase = ["+" + target[j]] + func(i, j+1)
            # If there are multiple answers, use the answer that favors removing from the source first. <= it came from the condition
            path = deleteCase if len(deleteCase) <= len(addCase) else addCase
        return path
    return func(0, 0)


source = "AVDSSD"
target = "ASDF"

test = diffBetweenTwoStrings(source, target)
print(test)


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
                                                                       add everything from target = source.length + target.length
"""


def array_of_array_products(arr):
    # divide left and right => for cumulated value
    if len(arr) <= 1:
        return []

    left = right = [1]
    print("line 63", left, right)
    for i in range(len(arr) - 1):
        left.append(left[-1] * arr[i])

    for j in range(len(arr) - 1, 1):
        right.insert(0, right[-1] * arr[j])

    print(left, right)

    return left

input = [2,2]
print(array_of_array_products(input))