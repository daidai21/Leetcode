# Runtime: 68 ms, faster than 76.33% of Python3 online submissions for Maximum Gap.
# Memory Usage: 14.7 MB, less than 33.33% of Python3 online submissions for Maximum Gap.
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_gap = 0
        for i in range(len(nums) - 1):
            max_gap = max(max_gap, nums[i + 1] - nums[i])
        return max_gap


# Runtime: 72 ms, faster than 56.91% of Python3 online submissions for Maximum Gap.
# Memory Usage: 14.8 MB, less than 33.33% of Python3 online submissions for Maximum Gap.
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        return max([0] + [nums[i] - nums[i - 1] for i in range(1, len(nums))])


# Runtime: 64 ms, faster than 89.89% of Python3 online submissions for Maximum Gap.
# Memory Usage: 15 MB, less than 33.33% of Python3 online submissions for Maximum Gap.
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        max_num, min_num = max(nums), min(nums)
        size = (max_num - min_num) // (len(nums) - 1) or 1  # bucket size
        bucket = [[None, None] for _ in range((max_num - min_num) // size + 1)]
        for num in nums:
            b = bucket[(num - min_num) // size]
            b[0] = num if b[0] is None else min(b[0], num)  # update min
            b[1] = num if b[1] is None else max(b[1], num)  # update max
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0] - bucket[i - 1][1] for i in range(1, len(bucket)))
