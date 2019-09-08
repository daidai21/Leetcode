# dp + recursion (top to down)
# Runtime: 688 ms, faster than 26.38% of Python3 online submissions for Burst Balloons.
# Memory Usage: 13.6 MB, less than 55.82% of Python3 online submissions for Burst Balloons.
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        def calculate(nums, dp, left, right):
            if dp[left][right] or right == left + 1: return dp[left][right]
            coins = 0
            for mid in range(left + 1, right):
                coins = max(coins, nums[left] * nums[mid] * nums[right] + calculate(nums, dp, left, mid) + calculate(nums, dp, mid, right))
            dp[left][right] = coins
            return coins

        return calculate(nums, dp, 0, n - 1)


# dp + three for (down to top)
# Runtime: 424 ms, faster than 76.29% of Python3 online submissions for Burst Balloons.
# Memory Usage: 13.5 MB, less than 65.96% of Python3 online submissions for Burst Balloons.
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for gap in range(2, n):
            for left in range(n - gap):
                right = left + gap
                for mid in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[mid] * nums[right] + dp[left][mid] + dp[mid][right])
        return dp[0][-1]


# dp: row is left, column is right
