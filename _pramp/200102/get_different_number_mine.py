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


# Time: O(n)
# Space: O(n)
def get_different_number(arr):
    elements = set(arr)
    for i in range(len(arr)):
        if i not in elements:
            return i
    return len(arr)


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
    n = len(arr)
    for i in range(len(arr)):
        tmp = arr[i]
        while tmp < n and arr[tmp] != tmp:
            arr[tmp], tmp = tmp, arr[tmp]

    print("arr changed to => ", arr)

    for j in range(len(arr)):
        if j != arr[j]:
            return j

    return n


arr = [0, 1, 3, 4]  # arr will be => [0,1,3,3]
test = get_different_number(arr)
print(test)


