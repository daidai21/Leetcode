class Solution:
    def longestConsecutive(self, nums: 'List[int]') -> 'int':
        if len(nums) < 1: return 0
        nums.sort()
        longest, tmp = 1, 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    tmp += 1
                else:
                    longest = max(longest, tmp)
                    tmp = 1
        return max(longest, tmp)
