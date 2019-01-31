class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]: i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]: j -= 1
            nums[i], nums[j] = nums[j], nums[i]  # 交换
        # 反转
        i, j = i + 1, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1


'''
解题思路：
首先从右向左遍历数组，找到第一个相邻的左<右的数对，记右下标为x，则左下标为x - 1
若x > 0，则再次从右向左遍历数组，直到找到第一个大于nums[x - 1]的数字为止，记其下标为y，交换nums[x - 1], nums[y]
最后将nums[x]及其右边的元素就地逆置
'''