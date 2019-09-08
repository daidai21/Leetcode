class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)
        while i < j:
            if nums[i] == 0:
                nums.append(0)
                nums.pop(i)
                j -= 1
            else:
                i += 1


'''
当遇到0时删除0并在尾部加上0
'''
