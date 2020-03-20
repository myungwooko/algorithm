# Time complexity O(n(m**2)
def deletion_distance(str1, str2):
  if not str1 and not str2:
    return 0

  count = 0
  li1 = list(str1) # Exactly In here, set() will not be most proper data structure for the reason about accessing element
  li2 = list(str2) # But FYI(not for this case), using "in" is much better with. => "a in list O(N) vs a in set O(1)"

  idx = 0
  while idx < len(li1):
    if li1[idx] not in li2:
      li1.pop(idx)
      count += 1
    else:
      idx += 1

  idx = 0
  while idx < len(li2):
    if li2[idx] not in li1:
      li2.pop(idx)
      count += 1
    else:
      idx += 1

  if li1 != li2:
    #return len(li1)
    while li1 != li2:
      ele = li1.pop(0)
      li2.remove(ele)
      count += 2
  return count


