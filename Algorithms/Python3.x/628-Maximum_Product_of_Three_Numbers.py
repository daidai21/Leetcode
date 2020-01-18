from typing import List


# Runtime: 332 ms, faster than 6.65% of Python3 online submissions for Maximum Product of Three Numbers.
# Memory Usage: 14 MB, less than 66.67% of Python3 online submissions for Maximum Product of Three Numbers.
################################################################################
# sort
################################################################################
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])


# Runtime: 280 ms, faster than 58.99% of Python3 online submissions for Maximum Product of Three Numbers.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Maximum Product of Three Numbers.
################################################################################
# single scan
# from small to big: min1, min2, max3, max2, max1
################################################################################
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = min2 = float("inf")
        max1 = max2 = max3 = float("-inf")
        for num in nums:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num
            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num >= max3:
                max3 = num
        return max(min1 * min2 * max1, max1 * max2 * max3)


print(Solution().maximumProduct([1,2,3]))  # 6
print(Solution().maximumProduct([1,2,3,4]))  # 24
