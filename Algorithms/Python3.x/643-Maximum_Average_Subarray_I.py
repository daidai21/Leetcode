# prefix sum array
# Runtime: 976 ms, faster than 54.91% of Python3 online submissions for Maximum Average Subarray I.
# Memory Usage: 16.3 MB, less than 12.50% of Python3 online submissions for Maximum Average Subarray I.
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pre_nums = [0]
        for num in nums:
            pre_nums.append(pre_nums[-1] + num)
        max_sum = float("-inf")
        for i in range(len(nums) - k + 1):
            max_sum = max(max_sum, pre_nums[i + k] - pre_nums[i])
        return max_sum / k


# Runtime: 920 ms, faster than 88.36% of Python3 online submissions for Maximum Average Subarray I.
# Memory Usage: 16.1 MB, less than 12.50% of Python3 online submissions for Maximum Average Subarray I.
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_k = sum(nums[:k])
        result = sum_k;
        for i in range(k, len(nums)):
            sum_k += nums[i] - nums[i - k]
            result = max(result, sum_k)
        return result / k
