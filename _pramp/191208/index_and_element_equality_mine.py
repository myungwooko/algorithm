#basically from some point, if value is greater than its index it's not possible to find matching one.


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

# O(logN)
def index_equals_value_search(arr):
  res = []
  lo, hi = 0, len(arr) - 1
  while lo <= hi:
    m = (lo + hi) // 2
    if arr[m] >= m:
      if arr[m] == m:
        res.append(m)
      hi = m - 1 
    else:
      lo = m + 1 
  if res:
    return res[-1]
  else:
    return -1

"""
 arr = [-8,0,2,5,9]
         0,1,2,3,4
lo    0 
hi    4
m     2
a[m]  2 
"""


