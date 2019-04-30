# 双指针
# Runtime: 40 ms, faster than 100.00%
# Memory Usage: 7 MB, less than 97.28%
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        area = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    area += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    area += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return area
