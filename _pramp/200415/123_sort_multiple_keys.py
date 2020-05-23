# sort with multiple keys
list = [[12, 'tall', 'blue', 1], [2, 'short', 'red', 9], [4, 'tall', 'blue', 13]]
s = sorted(list, key=lambda x: (x[0], -x[3]))
print(s)

# simple reverse
list = [5,4,3,2,2,8,7]
s = sorted(list, reverse=True)
print(s)