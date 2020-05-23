# c(x) = c(x-1) + c(x-2)
def c(x):
    if x <= 2:
        return x
    return c(x-1) + c(x-2)

test = c(10)
print(test)