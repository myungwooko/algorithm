"""
Bracket Match
A string of brackets is considered correctly matched if every opening bracket in
 the string can be paired up with a later closing bracket, and vice versa.
 For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t.
 For instance, “((” could become correctly matched by adding two closing
 brackets at the end, so you’d return 2.

Given a string that consists of brackets, write a function bracketMatch that
takes a bracket string as an input and returns the minimum number of brackets
you’d need to add to the input in order to make it correctly matched.

Explain the correctness of your code,
and analyze its time and space complexities.

Examples:

input:  text = “(()”
output: 1

input:  text = “(())”
output: 0

input:  text = “())(”
output: 2
Constraints:

[time limit] 5000ms

[input] string text

1 ≤ text.length ≤ 5000
[output] integer
"""
"""
Actual = 4
Expected = 0

  "(((((((((((((("      
     ^ 
stack = [(
count = 2
"""


# Time complexity: O(n*something)
# Space complexity: O(n)
def bracket_match(text):
    opener = []
    counter = 0
    for b in text:
        if b == '(':
            opener.append(b)
        else:
            if opener:
                opener.pop()
            else:
                counter += 1
    return counter + len(opener)


# Time complexity: O(n)
# Space complexity: O(1)
# Making list does not neccessary.
def bracket_match(text):
    open_b = 0
    result = 0
    for b in text:
        if b == '(':
            open_b += 1
        else:
            if open_b:
                open_b -= 1
            else:
                result += 1
    return result + open_b
