"""
# have to find none negative integer
# we are not sure the array is sorted

time O(NlogN), space O(1)
"""
def get_different_number(arr):
  arr.sort()
  smallest = arr[0]
  if smallest: #=> no zero
    return 0
  else:
    # be careful about list out of index
    for i in range(len(arr)-1):
      if arr[i] + 1 != arr[i+1]:
        return arr[i]+1
    return arr[-1] + 1

def firstMissingPositive(self, nums):
    nums.sort()
    res = 1
    for num in nums:
        if num == res:
            res += 1
    return res

a = [0,1,2,3,4,5]
print(get_different_number(a))



