"""
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

"""
Our purpose is looking for the root(* value is decimal point => binary search with decimal point - no problem)
"""

# Time complexity O(logN)
# Space complexity O(1)
def root(x, n):
    if x == 0: return 0
    # anyway it is not 0 but we use it as we want to search maximum arrange
    lower_bound = 0
    # if numerator is smaller than denominator, below formula can't be applied. 2^2 => 4(커짐) | (1/2)^2 = 1/4(작아짐)
    # The Minimum of x has to be 1
    # For maximum, if n = 1, the result will be the same with x. So upper_bound's max is x
    upper_bound = max(1, x)
    # approximate "root"
    approx_root = (lower_bound + upper_bound) / 2

    # approx_root - lower_bound == upper_bound - approx_root
    # make the condition with any one of them doesn't matter
    # , 그리고 처음에도 그 수도 차이 안나면 그건 같은 수나 마찬가지고 어쨌든 0과 그 범위안에는 무조건 있는 것(루트를 씌우면 어쩄든 작아지니까), => 근데 0.001보다 그 차이가 작으면 바로 그것을 return하면 됨.
    # 다음도 계속 그 범위안에 있는 건 매한가지이고 그러니 언제든 while만 만족시키지 않으면 바로 OK
    # , becuase covering root makes anyway the number smaller than before it definetley in the range.
    # so anyway if the condition does not satisfy while loop's condition => approx_root will be the root.
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


# simply we implement root()
# it has to be a function that has difference at most smaller than 0.001
def root(x, n):
    lower_bound, upper_bound = 0, max(1, x)
    approx_root = (lower_bound + upper_bound) / float(2)

    while approx_root - lower_bound >= 0.001:
        if pow(approx_root, n) < x:
            lower_bound = approx_root
        elif pow(approx_root, n) > x:
            upper_bound = approx_root
        else:
            break
        approx_root = (lower_bound + upper_bound) / float(2)

    return approx_root



