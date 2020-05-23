"""
Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order
to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them.
 Explain how your function works, and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
Constraints:

[input] string str1
[input] string str2
[output] integer
"""
# Time complexity: O(n+m) => n is for length of str1, m is for length of str2, Anyway k is definitely smaller than min(len(str1), len(str2)), doesn't need to be added
# Space complexity: O(n+m+2k)
def deletion_distance(str1, str2):
    a = set(str1)
    b = set(str2)
    count = 0

    next1 = []
    for c in str1:
        if c in b:
            next1.append(c)
        else:
            count += 1

    next2 = []
    for c in str2:
        if c in a:
            next2.append(c)
        else:
            count += 1

    i = 0
    while next1 != next2:
        if next1[i] != next2[i]:
            the_c = next1.pop(i)
            next2.remove(the_c)
            count += 2
        else:
            i += 1

    return count
