"""
Array of Array Products
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.

Examples:

input:  arr = [8, 10, 2]
output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

input:  arr = [2, 7, 3, 4]
output: [84, 24, 56, 42] # by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3]
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 20
[output] array.integer
"""
def array_of_array_products_brute(arr):
    res = []
    for i in range(len(arr)):
        mulplied = 1
        for j in range(len(arr)):
            if j == i:
                pass
            else:
                mulplied *= arr[j]
        res.append(mulplied)
    return res

arr = [2,7,3,4]
test = array_of_array_products_brute(arr)
print(test)



"""
[1, 2, 2*7, 2*7*3]

arr = [2,          7,          3,          4]
[1, 2, 2*7, 2*7*3]

arr = [2,          7,          3,          4]
res = [7 * 3 * 4,  2 * 3 * 4,  2 * 7 * 4,  2 * 7 * 3]

2 -> [1]       : [7, 3, 4]
7 -> [2]       : [3, 4]
3 -> [2, 7]    : [4]
4 -> [2, 7, 3] : [1]

좌우로 놓고 봤을때 이런식의 곱셈이 진행되기 때문에
이렇게 두개의 구조를 만든 다음
[1, 1*2, 1*2*7, 2*7*3], [1, 1*4, 1*4*3, 1*4*3*7]
"""
def array_of_array_products(arr):
    # arr =[2,7,3,4]
    if len(arr) <= 1:
        return []

    cumulative = [1]
    acc = 1
    for i in range(len(arr) - 1):
        acc *= arr[i]
        cumulative.append(acc)

    arrSec = arr[::-1] #쓸데없이 많은 일을 시키는 느낌.
    cumulativeRev = [1]
    acc = 1
    for i in range(len(arrSec) - 1):
        acc *= arrSec[i]
        cumulativeRev.append(acc)
    res = []
    for i in range(len(arr)):
        e1 = cumulative[i]
        e2 = cumulativeRev[-(i + 1)]
        res.append(e1 * e2)

    return res


arr = [2, 7, 3, 4]
test = array_of_array_products(arr)
print(test)


#mine
"""
Firstly, we don't concern the edge cases about making product like [], [1]
it shoud return just => 0 or along the instruction

* and this is the algorithm of O(N) time complexity
arr = [2,3,4,5]
We can split it like left and right side like below
    =>[(1)*3*4*5, (2)*4*5, (2*3)*5, (2*3*4)*1]
it means,
    left : right
     1     : 3,4,5
     2     : 4,5
     2,3   : 5
     2,3,4 : 1
and now we can see like each element is the product of left accumulated val and right accumulated val
so now we need to make that simple sources and then multiple along that direction pair.    
"""
def array_of_array_product(arr):
    accLeft = [1]
    acc = 1
    for i in range(len(arr)-1):
        acc *= arr[i]
        accLeft.append(acc)
    accRight = []
    acc = 1
    for i in range(len(arr), 0, -1):
        acc *= arr[i]
        accRight.insert(acc, 0)
    for i in range(len(arr)):
        arr[i] = accRight[i]*accLeft[i]
    return arr



def array_of_array_product(arr):
    if not arr or len(arr) == 1:
        return []
    l = [1]
    r = [1]
    for i in range(len(arr)-1):
        l_multiplier = arr[i]
        r_multiplier = arr[-(i+1)]
        l_turn = l[-1] * l_multiplier
        r_turn =  r[-1] * r_multiplier
        l.append(l_turn)
        r.append(r_turn)
    r = r[::-1]

    result = []
    for i in range(len(l)):
        result.append(l[i] * r[i])

    return result

arr = [2, 7, 3, 4]
"""
=>
   1 7x3x4x1  1x2 3x4x1, 1x2x7 4x1, 1x2x7x3 1
   l     r      l   r     l     r    l      r

=> We need to make 
l = [1, 1x2, 1x2x7, 1x2x7x3]
r = [1, 1x4, 1x4x3, 1x4x3x7]

=> then reverse r
=> and then just multiply it
"""
test = array_of_array_products(arr)
print(test)















