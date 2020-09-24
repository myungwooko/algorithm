"""
26. Remove Duplicates from Sorted Array
Easy

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""
"""
 # => 같으면 줄이고 인덱스도 하나 줄이고 다시
 # enumerate의 index 자체는 한번 바꾼다고 바꾼 걸로 적용되지 않는다.
 # 한번 조작해서 사용해도 그 다음순서에는 따로 적용을 하지 않으면 원래 자신의 순서의 인덱스를 사용
 # 어떤 밸류의 형태를 remove 하려고 할때, 완전히 같은 값이면 예를 들면 스트링이나 숫자 같은 원시 데이터면 앞에것이 삭제 된다.
                list.remove(nums[index]) <= 리스트 내에 같은 값이 있다면 앞의 것이 삭제된다.
                list.pop(index)          <= 리스트에서 정확히 해당 index의 값을 삭제한다.
 # while문은 i 가 자동으로 증가하지 않는다. 아래 버전 예시
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0

        index = 1
        while len(nums) > index:
            if nums[index - 1] == nums[index]:
                # nums.remove(nums[index])
                nums.pop(index)
            else:
                index += 1
        return len(nums)


"""  

while문은 i 가 자동으로 증가하지 않는다.

"""


class Solution:
    def removeDuplicates(self, num):

        i = 0
        while i in range(len(num) - 1):
            print(num[i], i)
            if (num[i] == num[i + 1]):
                num.remove(num[i])
            else:
                i += 1
            print(num)


s = Solution()
s.removeDuplicates([1, 2, 3, 3, 4, 5])

print(s)
