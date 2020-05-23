# c(x) = c(x-1) + c(x-2)
def c(x):
    if x <= 2:
        return x
    return c(x-1) + c(x-2)

test = c(10)
print(test)


#mine was
def c(x):
    count = [0]
    def helper(n):
        if n == x:
            count[0] += 1
        elif n < x:
            helper(n+1)
            helper(n+2)
    helper(0)
    return count[0]


test = c(10)
print(test)