'''
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_space = 0
        for start in range(len(height)):
            for end in range(start + 1, len(height)):
                max_space = max(max_space, min(height[start], height[end]) * (end - start))
        return max_space
'''


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_space, left, right = 0, 0, len(height) - 1
        while left < right:
            max_space = max(max_space, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]: 
                left += 1 
            else:
                right -= 1
        return max_space