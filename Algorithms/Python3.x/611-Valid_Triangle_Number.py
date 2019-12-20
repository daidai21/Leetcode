# Time Limit Exceeded
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
                        count += 1
        return count


# linear scan || greedy
# Runtime: 228 ms, faster than 99.22% of Python3 online submissions for Valid Triangle Number.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Triangle Number.
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        cnt = 0
        for i in range(len(nums) - 2):
            k = len(nums) - 1
            for j in range(i + 1, k):
                if j >= k:
                    break
                diff = nums[i] - nums[j]
                while nums[k] <= diff and k > j:
                    k -= 1
                cnt += k - j
        return cnt
