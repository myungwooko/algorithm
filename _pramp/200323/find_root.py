"""
Root of Number
Many times, we need to re-implement basic functions without using any standard library functions already implemented.
For example, when designing a chip that requires very little memory space.

In this question we’ll implement a function root that calculates the n’th root of a number.
The function takes a nonnegative number x and a positive integer n, and returns the positive n’th root of x within
an error of 0.001 (i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).

Don’t be intimidated by the question. While there are many algorithms to calculate roots that require prior knowledge
in numerical analysis (some of them are mentioned here), there is also an elementary method which doesn’t require more
than guessing-and-checking. Try to think more in terms of the latter.

Make sure your algorithm is efficient, and analyze its time and space complexities.

Examples:

input:  x = 7, n = 3
output: 1.913

input:  x = 9, n = 2
output: 3


In this question we’ll implement a function root
that calculates the n’th root of a number.
- The function takes a nonnegative number "x"
- a positive integer "n"
- returns the positive n’th root of x within an error of 0.001
(i.e. suppose the real root is y,
then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).

|y-root(x,n)| < 0.001).
|5.19615242271 - root(27, 2)| < 0.001

root(9, 2) = 3
root(27, 2) = 5.196   15242271
root(27, 3) = 3
root(8, 3) = 2
root(7, 3) = 1.913

pow(5.5, 2) = 30.25
pow(0.25, 2) = 1/2
   (1/4)^0.5 =  1/2
"""


# Time complexity O(logN)
# Space complexity O(1)
# Our purpose is looking for the root(* value is decimal point => binary search with decimal point - no problem)
def root(x, n):
    if x == 0: return 0

    # anyway it is not 0 but we use it as we want to search maximum arrange
    # for result value of root() <= root()의 결과값에 대한
    lower_bound = 0

    # For maximum, if n = 1, the result will be the same with x. So upper_bound's max is x
    # for result value of root() <= root()의 결과값에 대한
    upper_bound = max(1, x)

    # starting value of approximate value of result of root()
    approx_root = (lower_bound + upper_bound) / 2

    # approx_root - lower_bound == upper_bound - approx_root
    # make the condition with any one of them doesn't matter
    # , 그리고 처음에도 그 수도 차이 안나면 그건 같은 수나 마찬가지고, 그 다음부턴 공식에 따라 그 범위 안의 것일 수 밖에 없게 되므로
    # At the first time if the difference is smaller than that, that means those are assumed as almost same.
    # After the first time, along the formula it has to be in the range anyway.
    while (approx_root - lower_bound >= 0.001):

        # anyway difference is bigger than 0.001, keep decreasing the range till out of the while loop
        if pow(approx_root, n) > x:
            upper_bound = approx_root
        elif pow(approx_root, n) < x:
            lower_bound = approx_root
        else:
            break
        approx_root = float(upper_bound + lower_bound) / 2

    return approx_root


# it has to be a function that has difference at most smaller than 0.001
# lower_bound can't be zero though
# Time complexity: O(logn)
# Space complexity: O(1)
def root(x, n):
    lower_bound, upper_bound = 0, max(1, x)
    approx_root = (lower_bound + upper_bound) / float(2)

    while approx_root - lower_bound >= 0.001:
        calced = pow(approx_root, n)
        if calced < x:
            lower_bound = approx_root
        elif calced > x:
            upper_bound = approx_root
        else:
            break
        approx_root = (lower_bound + upper_bound) / float(2)

    return approx_root


# Time complexity: O(log(n))
# Space complexity: O(1)
# Just tried to use lambda. It looks not useful here though.
def root(x, n):
    upper_bound = x
    lower_bound = 0
    get_possible_root = lambda lower_bound, upper_bound: (lower_bound +
                                                          upper_bound) / 2
    possible_root = get_possible_root(lower_bound, upper_bound)
    while upper_bound - possible_root > 0.001:
        val = pow(possible_root, n)
        if val == x:
            return possible_root
        elif val < x:
            lower_bound = possible_root
        else:
            upper_bound = possible_root
        possible_root = get_possible_root(lower_bound, upper_bound)
    # Unlike Pramp need to do
    return round(possible_root, 3)


# Time complexity: O(logn)
# Space complexity: O(1)
def root(x, n):
    upper_bound = x
    lower_bound = 0
    approx_root = (upper_bound + lower_bound) / 2
    while approx_root - lower_bound > 0.001:
        v = pow(approx_root, n)
        if v == x:
            return approx_root
        elif v < x:
            lower_bound = approx_root
        else:
            upper_bound = approx_root
        approx_root = (upper_bound + lower_bound) / 2
    return round(approx_root, 3)


# Time complexity: O(logn)
# Space complexity: O(1)
def root(x, n):
    # sr = square root
    min_sr = 0
    max_sr = x
    get_possible_root = lambda min_sr, max_sr: (min_sr + max_sr) / float(2)
    possible_root = get_possible_root(min_sr, max_sr)
    while max_sr - possible_root > 0.001:
        v = pow(possible_root, n)
        if v == x:
            return possible_root
        elif v < x:
            min_sr = possible_root
        else:
            max_sr = possible_root
        possible_root = get_possible_root(min_sr, max_sr)
    return round(possible_root, 3)


# Tests
x = 7
n = 3
test = root(x, n)
print(test)
print(test == 1.913)

x = 9
n = 2
test = root(x, n)
print(test == 3)
