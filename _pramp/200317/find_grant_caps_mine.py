"""
Award Budget Cuts
The awards committee of your alma mater (i.e. your college/university) asked for your assistance with a budget allocation
 problem they’re facing. Originally, the committee planned to give N research grants this year.
 However, due to spending cutbacks, the budget was reduced to newBudget dollars and now they need to reallocate the grants.
 The committee made a decision that they’d like to impact as few grant recipients as possible by applying a maximum cap on all grants.
 Every grant initially planned to be higher than cap will now be exactly cap dollars. Grants less or equal to cap, obviously, won’t be impacted.

Given an array grantsArray of the original grants and the reduced budget newBudget, write a function findGrantsCap that
finds in the most efficient manner a cap such that the least number of recipients is impacted
and that the new budget constraint is met (i.e. sum of the N reallocated grants equals to newBudget).

Analyze the time and space complexities of your solution.

Example:

input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190

output: 47 # and given this cap the new grants array would be
           # [2, 47, 47, 47, 47]. Notice that the sum of the
           # new grants is indeed 190
Constraints:

[time limit] 5000ms

[input] array.double grantsArray

0 ≤ grantsArray.length ≤ 20
0 ≤ grantsArray[i]
[input] double newBudget

[output] double
"""
"""

maximum cap on all grants
Every grant initially planned to be higher than cap
Grants less or equal to cap, obviously, won’t be impacted.


ex1)
grantsArray = [8,7,2,5,9], newBudget = 20
              [2,5,7,8,9]

              20 - 2 => 18/4 => cap 4.5

- roughCap => 20/5  => 4.0
- one(2) can be excluded because it is definitely not impacted by cutting budget
- rough2Cap => so 20/4 => 5.0
- one(5) can be excluded because it is definitely not impacted by cutting budget
- 20/3 => 6.66666666
- cap => 5 cap


ex2)
grantsArray = [8,7,2,5,9], newBudget = 4

4/5 => 0.8
=> 0.8


ex3)
grantsArray = [8,7,2,5,9], newBudget = 30
30/5 => 6.0 => 2,5
30 - (2+5) => 23
23/3 => cap 7.6
23-7 => 16
16/2 => 8.0
[8, 7, 2, 5, 8]


[8,7,2,5,9] 20

[2,5,7,8,9] 20 
20/5 => 4

2

available = 20 -2 = 18 / 4 = 4.5



Binary search
https://leetcode.com/problems/koko-eating-bananas/

"""
"""

maximum cap on all grants
Every grant initially planned to be higher than cap
Grants less or equal to cap, obviously, won’t be impacted.


ex1)
grantsArray = [8,7,2,5,9], newBudget = 20
              [2,5,7,8,9]

              20 - 2 => 18/4 => cap 4.5

- roughCap => 20/5  => 4.0
- one(2) can be excluded because it is definitely not impacted by cutting budget
- rough2Cap => so 20/4 => 5.0
- one(5) can be excluded because it is definitely not impacted by cutting budget
- 20/3 => 6.66666666
- cap => 5 cap


ex2)
grantsArray = [8,7,2,5,9], newBudget = 4

4/5 => 0.8
=> 0.8


ex3)
grantsArray = [8,7,2,5,9], newBudget = 30
30/5 => 6.0 => 2,5
30 - (2+5) => 23
23/3 => cap 7.6
23-7 => 16
16/2 => 8.0
[8, 7, 2, 5, 8]


[8,7,2,5,9] 20

[2,5,7,8,9] 20 
20/5 => 4

2

available = 20 -2 = 18 / 4 = 4.5



Binary search
https://leetcode.com/problems/koko-eating-bananas/

"""
"""

maximum cap on all grants
Every grant initially planned to be higher than cap
Grants less or equal to cap, obviously, won’t be impacted.


ex1)
grantsArray = [8,7,2,5,9], newBudget = 20
              [2,5,7,8,9]

              20 - 2 => 18/4 => cap 4.5

- roughCap => 20/5  => 4.0
- one(2) can be excluded because it is definitely not impacted by cutting budget
- rough2Cap => so 20/4 => 5.0
- one(5) can be excluded because it is definitely not impacted by cutting budget
- 20/3 => 6.66666666
- cap => 5 cap


ex2)
grantsArray = [8,7,2,5,9], newBudget = 4

4/5 => 0.8
=> 0.8


ex3)
grantsArray = [8,7,2,5,9], newBudget = 30
30/5 => 6.0 => 2,5
30 - (2+5) => 23
23/3 => cap 7.6
23-7 => 16
16/2 => 8.0
[8, 7, 2, 5, 8]


[8,7,2,5,9] 20

[2,5,7,8,9] 20 
20/5 => 4

2

available = 20 -2 = 18 / 4 = 4.5



Binary search
https://leetcode.com/problems/koko-eating-bananas/

"""


def find_grants_cap(grantsArray, newBudget):
    def helper(lis, budget):
        beforeLen = len(lis)
        # Because at Python2 3/2 => 1
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


# Time complexity: O(n) n is number of calling the helper function. But actually exponential bc call stack.
# Space complexity: O(n) making nextB's sum
def find_grants_cap(grantsArray, newBudget):
    def helper(arr, budget):
        cap = budget / float(len(arr))
        nextB = []
        for e in arr:
            if e <= cap:
                budget -= e
            else:
                nextB.append(e)
        if len(arr) == len(nextB):
            return cap
        return helper(nextB, budget)

    return helper(grantsArray, newBudget)


# Time complexity: O(n^2), not exponential
# Space complexity: O(n)
def find_grants_cap(grantsArray, newBudget):
    queue = [(grantsArray, newBudget)]
    while queue:
        grants, budget = queue.pop(0)
        cap = float(budget) / len(grants)
        next_grants = []
        for g in grants:
            if g >= cap:
                next_grants.append(g)
            else:
                budget -= g
        if len(next_grants) == len(grants) or not next_grants:
            return cap
        else:
            queue.append((next_grants, budget))
    return


# Time complexity: O(n)
# Space complexity: O(n)
def find_grants_cap(grantsArray, newBudget):
    curr_arr = grantsArray
    curr_budget = newBudget
    while True:
        curr_ave = curr_budget / float(len(curr_arr))
        next_arr = []
        for e in curr_arr:
            if e <= curr_ave:
                curr_budget -= e
            else:
                next_arr.append(e)
        if not next_arr or next_arr == curr_arr:
            return curr_ave
        curr_arr = next_arr
    return
