class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i, _ in enumerate(nums):
            j, k = i + 1, len(nums) - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == target:
                    return three_sum
                elif abs(three_sum - target) < abs(res - target):
                    res = three_sum
                elif three_sum < target:
                    j += 1
                elif three_sum > target:
                    k -= 1
                else:
                    return three_sum
        return res