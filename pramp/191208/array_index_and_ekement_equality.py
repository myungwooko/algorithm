# O(N)
def index_equals_value_search(arr):
    if not arr or len(arr) > 100:
        return -1
    for i, v in enumerate(arr):
        if v > i:
            return -1
        if i == v:
            return i
    return -1

"""
# O(logN)
def index_equals_value_search(arr):
  res = []
  lo, hi = 0, len(arr) - 1
  while lo <= hi:
    m = (lo + hi) // 2
    if arr[m] == m:
      res.append(m)
      hi = m - 1 
    if arr[m] > m:
      return -1
    else:
      lo = m + 1 
  if res:
    return res[-1]
  else:
    return -1
"""



"""
# arr1 = [1,2,3,4,5] => 
# 1,2,3,4,5
# 0,1,2,3,4

"""
