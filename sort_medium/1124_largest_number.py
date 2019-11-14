"""
179. Largest Number
Medium

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

=================================================================================
compare를 통해서 이런식으로 sorting
input = [41,23,87,55,50,53,18,9, 0, 0] => [9, 87, 55, 53, 50, 41, 23, 18, 0, 0]
앞의 숫자가 큰순으로

lstrip('0')Remove leading 0s, if empty return '0'.
 return ''.join(nums).lstrip('0') or ‘0'


=> nums = '0023'
=> ''.join(nums).lstrip('0')
'23'
=> nums = '2003'
=> ''.join(nums).lstrip('0')
'2003'
=> nums = ['0', '0', '2']
=> ''.join(nums).lstrip('0')
‘2'

Only string not list
=> nums.lstrip('0')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'lstrip'



"""
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        def cmp_func(x, y):
            """Sorted by value of concatenated string increasingly."""
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        # Build nums contains all numbers in the String format.
        nums = list(map(str, nums))

        # Sort nums by cmp_func decreasingly.
        nums.sort(key=cmp_to_key(cmp_func), reverse=True)

        # Remove leading 0s, if empty return '0'.
        return ''.join(nums).lstrip('0') or '0'

    # bubble sort
    def largestNumber2(self, nums):
        # forLoop_1: len - 1 번 만큼 for loop을 처음부터 해결한지점 전까지 계속 반복해야 하고
        # forLoop_2: 끝에 정리된거는 제외하면 되기 때문에 때문에
        for i in range(len(nums), 0, -1):
            for j in range(i - 1):
                if not self.compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return str(int("".join(map(str, nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)


input = [41,23,87,55,50,53,18,9, 0, 0]
s = Solution()
test = s.largestNumber(input)
print(test)

