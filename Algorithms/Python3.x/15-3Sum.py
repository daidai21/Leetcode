class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        matrix = []  # 返回的数组
        for i in range(len(nums) - 1):
            left, right = i + 1, len(nums) - 1
            while left < right:
                add = nums[i] + nums[left] + nums[right]
                if add == 0 and [nums[i], nums[left], nums[right]] not in matrix:
                    matrix.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right - 1
                elif add < 0: left += 1
                else: right -= 1
        return matrix

