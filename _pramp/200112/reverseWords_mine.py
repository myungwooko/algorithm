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


# Time Complexity: O(n)
# Space complexity: O(1)
def reverse_words(arr):
    arr = arr[::-1]
    last_idx = len(arr) - 1

    for i in range(len(arr)):
        if arr[i] == ' ':
            continue

        if i == 0 or (i > 0 and arr[i - 1] == ' '):
            left = i

        # the condition of 'left' part dosen't need to be added because left must have been set before 'right'
        # but wanted to show it explicitly so that it can help understanding easily.
        if (left == 0 or left) and (i < last_idx
                                    and arr[i + 1] == ' ') or i == last_idx:
            right = i
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
    return arr


arr = [
    'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p',
    'r', 'a', 'c', 't', 'i', 'c', 'e'
]

test = reverse_words(arr)
print(test)
