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


# Time complexity: O(n+m+sum^2)
# sum^2 => It covers for pop and remove part
# Space complexity: O(n+m+sum*2)
def deletion_distance(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    count = 0

    filtered1 = []
    for c in str1:
        if c in set2:
            filtered1.append(c)
        else:
            count += 1

    filtered2 = []
    for c in str2:
        if c in set1:
            filtered2.append(c)
        else:
            count += 1

    idx = 0
    while filtered1 != filtered2:
        curr = filtered1[idx]
        if filtered2[idx] != curr:
            filtered1.pop(idx)
            filtered2.remove(curr)
            count += 2
        idx += 1

    return count


# Time Complexity: O(n+m+smaeToOrder^2)
# Space Complexity: O(max(m, n))
def deletion_distance(str1, str2):
    setA = set(str1)
    setB = set(str2)
    listA = []
    listB = []
    count = 0

    for c in str1:
        if c in setB:
            listA.append(c)
        else:
            count += 1

    for c in str2:
        if c in setA:
            listB.append(c)
        else:
            count += 1

    idx = 0
    while listA != listB:
        curr = listA[idx]
        if listA[idx] == listB[idx]:
            idx += 1
        else:
            listA.remove(curr)
            listB.remove(curr)
            count += 2

    return count


# Time complexity: O(k^2) Because total different order case will iterate total length of common length and also iterate n for remove().
# Space complxity: O(max(m, n))
def deletion_distance(str1, str2):
    result = 0
    set1 = set(str1)
    set2 = set(str2)
    surv1 = []
    surv2 = []

    for i, v in enumerate(str1):
        if v in set2:
            surv1.append(v)
        else:
            result += 1

    for i, v in enumerate(str2):
        if v in set1:
            surv2.append(v)
        else:
            result += 1

    idx = 0
    while surv1 != surv2:
        curr = surv1[idx]
        if surv1[idx] == surv2[idx]:
            idx += 1
        else:
            # surv1.remove(surv1[idx])
            # surv1.remove(surv1[idx]) <= after the execution above, it points different value or it can raise index error.
            surv1.remove(curr)
            surv2.remove(curr)
            result += 2

    return result
