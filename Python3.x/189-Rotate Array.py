class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        k = k % len_nums
        tmp = []
        for i in range(len_nums - k, len_nums):
            tmp.append(nums[i])
        for i in range(len_nums - 1, 0, -1):
            nums[i] = nums[i - k]
        for i in range(k):
            nums[i] = tmp[i]