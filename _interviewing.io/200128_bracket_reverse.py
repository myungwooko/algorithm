"""
You are given a string that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching brackets, starting from the innermost one.

Your result should not contain any brackets.


Example 1:

Input: s = "(abcd)"
Output: "dcba"

Example 2:

Input: s = "(oi(love)ew)"
Output: "weloveio"

Explanation: The substring "love" is reversed first, then the whole string is reversed.





######################################################
logic - complex and not clear

( - right
) - left

ghj(jkhgj)h(j(jhjk)a)kk =>
    ^
stack = [(]
curr = "a" # => if we meet left opened bracket we have to reverse the curr

                if we meet left opened bracket and stack is empty we put the curr to words and then reverse it => then we can add it to result

words = ["j", "kjhj", "a"]
        ajhjkj


result = "ghj"+ "jghkj" + "h" + "ajhjkj" + "kk"

1. put left bracket in 
2. we accumulate the characters inside of it
3. when we face right bracket the accumalated charters => reverse

stack = []
curr = "ew"
strs = ["oi", evol, ew] => join => reverse => weloveio 
#######################################################
"""


"""
Worse approach made if else hell. 
That made it really complex.
Even though it looks right, it is too complex, that means there can be simpler righty option out there.
So in that case, try make it simpler => if it can be simpler => try to find another approach.
make it simpler => Everything is possible.
"""
def reverseInside(s):
    stack = []
    curr = ""
    words = []
    result = ""
    for i in s:
        if not stack and i.isalpha():
            result += i

        elif stack and i.isalpha():
            curr += i

        elif i == "(":
            if curr:
                words.append(curr)
                print(73, words)
                curr = ""
            stack.append(i)
        elif i == ")":
            stack.pop()

            if not stack:
                if words:
                    words.append(curr)
                    joined = "".join(words)
                    reverse = joined[::-1]
                    words = []
                else:
                    reverse = curr[::-1]
                    # if words.append(reverse)
                curr = ""
            else:
                reverse = curr[::-1]
                # result += reverse
            result += reverse
    return result

s1 = "(abcd)"
test1 = reverseInside(s1)
print(test1 == "dcba")

s2 = "(oi(love)ew)"
test2 = reverseInside(s2)
print(test2=="weloveio")



"""
simply, stack에 쌓아나가다가 => ")"나오면 "(" 전까지 pop()으로 계속 붙여서 stack에 쌓여있는 것에 다시 넣으면 된다.
Simply, accumulate stack and when meet ")", before last "(" in stack => pop value and accumulate it and then add it to stack. Just like that.
"""

def bracketReverse(s):
    stack = []
    for i in s:
        if i != ")":
            stack.append(i)
        else:
            acc = []
            while stack[-1] != "(":
                acc.append(stack.pop())
            stack.pop()
            stack += acc
    return "".join(stack)


s1 = "(abcd)"
test1 = bracketReverse(s1)
print(129, test1 == "dcba")

s2 = "(oi(love)ew)"
test2 = bracketReverse(s2)
print(133, test2=="weloveio")




"""
Feedback

The candidate understands CS fundamentals and I certainly see potential in the candidate. To continue practicing, 
the candidate can continue working with these algorithmic patterns:

DFS/BFS
greedy
sliding window
divide and conquer
recursion
dynamic programming.

A popular site to practice algorithms is leetcode.com. To ensure practice conditions close to the _interview setting, I encourage
1. Code in a notepad
2. Setup a timer 
3. Talk during a practice
4. Create some psychological pressure, e.g. ask somebody to watch you during practice, record yourself on a video, etc.

To review topics of system design, the candidate can start from:
- https://github.com/donnemartin/system-design-primer
- https://github.com/checkcheckzz/system-design-_interview

"""


