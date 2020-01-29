"""
42. Trapping Rain Water
Hard

5416

104

Add to List

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water
(blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

detailed explanation
- At height[i], what is the maximum height from [0, i-1] and [i+1, len(height)-1]? Let us call these heights as max_left and max_right.
- What is the water trapped at height[i]?
- if max_left <= height[i] or max_right <= height[i], then water trapped is 0
- if max_left > height[i] and max_right > height[i], then water_trap += min(max_left, max_right)-height[i]
- You can use linear space and precompute max_right. max_left can be computed as we move left to right.
"""

class Solution:
    def trap(self, height):
        if not height:
            return 0
        max_right = [0] * len(height)

        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                max_right[i] = height[i]
            else:
                max_right[i] = max(height[i], max_right[i + 1])
        trapped, max_left = 0, height[0]
        for i in range(1, len(height)):
            if max_left > height[i] and max_right[i] > height[i]:
                trapped += min(max_left, max_right[i]) - height[i]
            max_left = max(height[i], max_left)
        return trapped


s = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
test = s.trap(input)
print(test)