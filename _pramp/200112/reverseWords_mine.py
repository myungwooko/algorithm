"""
Sentence Reverse
You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.

Example:

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
Constraints:

[time limit] 5000ms

[input] array.character arr

0 ≤ arr.length ≤ 100
[output] array.character

"""
"""
Brute Force: O(N) Time with O(N) Space

Space Saving Solution: O(N) Time with O(1) Space
         l
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
        'm', 'a', 'k', 'e', 's', '  ',
         p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
         r

         perfect makes practice
         l
                r
         ecitcarp sekam tcefrep
         practice makes perfect

1. arr[::-1]      
     "" => space = arr.pop(7) => arr.insert(0)
           char => arr.pop(theIndex) 
                => insIdx = 0 from to acc till meet space  

      [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
        'm', 'a', 'k', 'e', 's', '  ',
        'p', 'e', 'r', 'f', 'e', 'c', 't' ]

        => ["practice"]

Multiple Traversals
Multiple Pointers
variables l and r

"""


def reverse_words(arr):
    rev = arr[::-1]

    l = 0
    for i in range(len(rev)):
        if rev[i] == " " or i == len(rev) - 1:
            if i == len(rev) - 1:
                r = i
            else:
                r = i - 1

            while l < r:
                rev[l], rev[r] = rev[r], rev[l]
                l += 1
                r -= 1

            if i == len(rev) - 1:
                break

            # we do reverse process only for word, so we need to set l for exactly an alphabet character.
            l = i + 1
            while l < len(arr) and not arr[l]:
                l += 1

    return rev


def reverse_words(arr):
    rev = arr[::-1]

    l = 0
    for i in range(len(rev)):
        if rev[i] == " " or i == len(rev) - 1:
            if i == len(rev) - 1:
                r = i
            else:
                r = i - 1

            while l < r:
                rev[l], rev[r] = rev[r], rev[l]
                l += 1
                r -= 1

            if i == len(rev) - 1:
                break

            l = i + 1
            while l < len(rev) and not rev[l]:
                l += 1

    return rev


# def reverse_words(s):
#     rev = s[::-1]
#     for i in range(len(rev)):
#         if i == 0 or (i > 0 and not rev[i-1].isalpha()):
#             start = i
#         elif i == len(rev) - 1 or not rev[i+1].isalpha():
#             end = i
#             while start < end:
#                 rev[start], rev[end] = rev[end], rev[start]
#                 start += 1
#                 end -= 1
#     return rev


arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ',
        'm', 'a', 'k', 'e', 's', ' ',
        'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

test = reverse_words(arr)
print(test)
