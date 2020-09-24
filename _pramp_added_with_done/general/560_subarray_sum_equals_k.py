"""
560. Subarray Sum Equals K
Medium

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
"""
Let's remember count[V], the number of previous prefix sums with value V. If our newest prefix sum has value W, and W-V == K, then we add count[V] to our answer.

This is because at time t, A[0] + A[1] + ... + A[t-1] = W, and there are count[V] indices j with j < t-1 
and A[0] + A[1] + ... + A[j] = V. Thus, there are count[V] subarrays A[j+1] + A[j+2] + ... + A[t-1] = K.

- key는 sum
- 순회하다가 sum-k = 0이 될때를 만나면 value값인 해당 count를 더해준다.
- 아하! 계속 축적 되었던 거고 그 축적값에서 k를 뺀값이 그 전에 있으면! 거기부터 해당 축적까지 딱 k만큼 온거니깐!!
- 그래서 축적값-k를 해서 나온값이 지나온데에 있으면 count를 증가 시켜줬던 거였구나!!!!!!!
"""


class Solution:
    def subarraySum(self, nums, k):
        count = 0
        sumVal = 0
        hashMap = {}
        hashMap[0] = 1
        for i in nums:
            sumVal += i
            if sumVal - k in hashMap:
                count += hashMap[sumVal - k]
            # key는 유일하니깐 똑같은 값의 형태로 count를 올리게 되면 update를 해줘야 한다.
            hashMap[sumVal] = hashMap.get(sumVal, 0) + 1
        return count
