def find_grants_cap(grantsArray, newBudget):
    def helper(lis, budget):
        beforeLen = len(lis)
        #Because at Python2 3/2 => 1
        ave = float(budget) / len(lis)
        for i, v in enumerate(lis):
            if v <= ave:
                e = lis.pop(i)
                budget -= e
        if len(lis) == beforeLen or not lis:
          if ave == int(ave):
            return int(ave)
          return ave
        return helper(lis, budget)
    return helper(grantsArray, newBudget)


grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190
#output: 47

test = find_grants_cap(grantsArray, newBudget)
print(test)
