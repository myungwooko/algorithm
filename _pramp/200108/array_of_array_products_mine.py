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

arr = [2, 7, 3, 4]
test = array_of_array_products(arr)
print(test)











