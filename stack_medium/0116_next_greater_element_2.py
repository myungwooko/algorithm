"""
503. Next Greater Element II
Medium

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater
Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next
in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""
class Solution(object):
    # Time Limit Exceeded
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) > 10000:
            return
        res = []
        idx = 0
        while idx < len(nums):
            stack = []
            circulration = nums[idx + 1:] + nums[:idx]
            for num in circulration:
                if num > nums[idx]:
                    stack.append(num)
                    break
            if not stack:
                res.append(-1)
            else:
                res.append(stack[0])
            idx += 1
        return res


    # 두바퀴로 서클을 돌수 있는 환경을 만들고 => 자신보다 큰 수가 자신보다 뒤에 있지 않고 앞에 있는 경우에 대한 비교를 해줘야 하므로.
    # 마지막에 지난애가 최신의 것으로서 stack에 쌓이게 된다. 자신의 순서로서 자신보다 큰수를 찾기 위해 비교를 해야하니깐.
    # stack에 같이 쌓여있는 것들은 그 전의 stack에 쌓여있는 것보다 최신의 stack에 들어온것이 크지 못했기 때문이다.
    # 결국 stack에 있는 것들은 모두 큰것들을 만나지 못한 것들이 된다.
    # 큰걸 만나면 그게 만족되는한에서 계속 적용 시켜준다. 왜냐면 안나가고 남아있다는건 자신보다 큰걸 만나지 못했다는거고 이것이 자신에게도 큰것일수 있는것이니까.
    # 어차피 순환으로서 순서는 자신 다음의 최초의 큰 수인게 맞는게 된다.
    # res는 그렇게 넣어주면 된다.

    # two cycle makes circular comparing environment => for checking case -> some number's nextGreaterElement is located before than the number.
    # last one is accumulated at last of stack. As its turn to find nextGreaterElements.
    # they are in stack togeher because the latest last of stack is not greater than former last of stack.
    # therefore those elements in stack are all the thing that didn't able to meet their nextGreaterElement.
    # when meet nextGreaterElement of last of the stack continuously apply inner content of while loop till it satisies conditions clause.
    # Becuase it is circular, nextGreaterElement is the last of stack's kind of next one and exactly first nextGreaterElement.
    # making res like that
    def nextGreaterElements(self, A):
        stack, res = [], [-1] * len(A)
        for _ in range(2):
            for i in range(len(A)):
                # while 문으로서 스택이 있고 A[i]가 큰 한에서는 계속 적용.
                while stack and A[stack[-1]] < A[i]:
                    print(stack, i)
                    res[stack.pop()] = A[i]
                stack.append(i)
        return res





nums = [3, 2, 1]
s = Solution()
test = s.nextGreaterElements(nums)
print(test)
# 012
# 0101

