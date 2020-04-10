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
def reverse_words(arr):
    rev = arr[::-1]
    start = 0
    for i in range(len(arr)):
        if rev[i] == " " or i == len(rev) - 1:
            if i == len(rev) - 1:
                end = i
            else:
                end = i - 1

            while start < end:
                rev[start], rev[end] = rev[end], rev[start]
                start += 1
                end -= 1

            if i == len(rev) - 1:
                return rev

            start = i + 1
            while start < len(rev) and rev[start] == " ":
                start += 1

    return rev

#
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
