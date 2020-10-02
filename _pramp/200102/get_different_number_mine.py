"""
Getting a Different Number
Given an array arr of unique nonnegative integers,
implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.

Even if your programming language of choice doesn’t have that restriction (like Python),
assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance,
the operation MAX_INT + 1 would be undefined in our case.

Your algorithm should be efficient, both from a time and a space complexity perspectives.

Solve first for the case when you’re NOT allowed to modify the input arr. If successful and still have time,
 see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed.
 Do so without trading off the time complexity.

Analyze the time and space complexities of your algorithm.

Example:

input:  arr = [0, 1, 2, 3]

output: 4
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ MAX_INT
0 ≤ arr[i] ≤ MAX_INT for every i, 0 ≤ i < MAX_INT
[output] integer
"""


# Time: O(nlogn)
# Space: O(1)
def get_different_number(arr):
    arr.sort()
    res = 0
    for i in arr:
        if i == res:
            res += 1
        else:
            break
    return res


# Time: O(n^2)
# Because "a not in arr" is excuted in for loop. ele in setA usually O(1) but in worst case it can be O(n)
# Space: O(n)
def get_different_number(arr):
    arr = set(arr)
    for i in range(len(arr)):
        if i not in arr:
            return i
    return len(arr) if len(arr) < pow(2, 31) - 1 else None


# Time: O(n)
# Space: O(1), in place
"""
# 우리는 무조건 0부터 count하므로 len 밖에것은 당연히 빼도 되고, 그곳은 중복된 수로 남아있게 된다. 하지만 관계 없다.
# 그렇지 않은 경우는 다음것을 tmp로서 계속해서 이어 받아나가면서 계속 제자리를 찾아가게 해준다.
# while loop 조건이 tmp < n이 아니면 그냥 버리는 개념.
# 해당 내부 while loop의 논리를 가지고 첫번짜 for loo을 진행하여 만든다. 
# 만약 0부터 쭉 이어지는 수라면 중복으로 남는것 없이 모두 자리를 찾아가게 될 것이고,
# 건너 뛴게 있다면(최대 index 범위 밖의 것이 존재하게 됨.) 그 범위 밖의 것은 없어지고, 범위 내의 수중 중복 된 부분이 있을 것이다. 
# 그렇게 만들고 두번째 for loop에서 0부터 차례대로 체크하여 없으면 그것을 return
# 다 돌면 마지막에 len(arr) => 추가 index를 return 
"""


def get_different_number(arr):
    max_int = pow(2, 31) - 1
    n = len(arr)
    for i in range(n):
        curr = arr[i]
        while curr < n and curr != arr[curr]:
            arr[curr], curr = curr, arr[curr]
            # tmp, arr[tmp] = arr[tmp], doesn't work
            # simply, 이런경우 indexing하는 것에 할당을 먼저 해준다는 개념으로 그것을 왼쪽으로서 먼저 위치 시키는 것으로 해결 위와 같이.
    for i in range(n):
        if i != arr[i]:
            return i
    return n if n < 2 ^ 31 else None


arr = [0, 1, 3, 4]  # arr will be => [0,1,3,3] in this case
test = get_different_number(arr)
print(test)
