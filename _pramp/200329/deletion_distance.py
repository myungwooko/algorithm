"""
Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings
in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance
between them. Explain how your function works, and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
"""


# Time complexity: O(n+m+k^2), n is for length of str1, m is for length of str2, k is for lenght of same characters
# Space complexity: O(n+m)
def deletion_distance(str1, str2):
    set_of_str1 = set(str1)
    set_of_str2 = set(str2)
    result_count = 0

    str1_surviive = []
    for c in str1:
        if c in set_of_str2:
            str1_surviive.append(c)
        else:
            result_count += 1

    str2_surviive = []
    for c in str2:
        if c in set_of_str1:
            str2_surviive.append(c)
        else:
            result_count += 1

    idx = 0
    while str1_surviive != str2_surviive:
        if str1_surviive[idx] != str2_surviive[idx]:
            diff = str1_surviive.pop(idx)
            str2_surviive.remove(diff)
            result_count += 2
        else:
            idx += 1

    return result_count
