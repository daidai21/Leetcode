# Runtime: 2088 ms, faster than 5.14% of Python3 online submissions for Partition to K Equal Sum Subsets.
# Memory Usage: 13.8 MB, less than 5.55% of Python3 online submissions for Partition to K Equal Sum Subsets.
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse=True)
        self.nums = nums
        sub_sum = sum(self.nums) // k
        self.sub_lst = [sub_sum] * k
        return self.dfs(0, len(nums), k)

    def dfs(self, idx, len_nums, k):  # dfs + backtracking
        if idx == len_nums:
            return True
        for i in range(k):
            if self.sub_lst[i] >= self.nums[idx]:
                self.sub_lst[i] -= self.nums[idx]
                if self.dfs(idx + 1, len_nums, k):
                    return True
                self.sub_lst[i] += self.nums[idx]
        return False
