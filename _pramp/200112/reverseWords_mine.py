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
def reverseWords(arr):
    if not arr:
        return arr
    rev = arr[::-1]
    start = 0
    for i in range(len(rev)):
        if i == len(rev) - 1 or rev[i+1] == "  ":
            rev = arrMirror(rev, start, i)
            if i < len(rev) - 1:
                start = i + 2
    return rev

def arrMirror(arr, start, end):
    l, r = start, end
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr


arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
        'm', 'a', 'k', 'e', 's', '  ',
        'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

test = reverseWords(arr)
print(test)
