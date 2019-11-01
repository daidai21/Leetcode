# Runtime: 432 ms, faster than 34.55% of Python3 online submissions for Largest Divisible Subset.
# Memory Usage: 13.8 MB, less than 20.00% of Python3 online submissions for Largest Divisible Subset.
# dp
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        len_subset = [0] * len(nums)
        parent = [None] * len(nums)
        max_len_subset = 0
        max_len_subset_num = 0
        for i in range(len(nums) -1, -1, -1):
            for j in range(i, len(nums)):
                if nums[j] % nums[i] == 0 and len_subset[i] < 1 + len_subset[j]:
                    len_subset[i] = 1 + len_subset[j]
                    parent[i] = j
                    if len_subset[i] > max_len_subset:
                        max_len_subset = len_subset[i]
                        max_len_subset_num = i
        ans = []
        for i in range(max_len_subset):
            ans.append(nums[max_len_subset_num])
            max_len_subset_num = parent[max_len_subset_num]
        return ans
