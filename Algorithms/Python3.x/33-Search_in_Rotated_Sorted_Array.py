class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target: return mid  # 找到
            if nums[mid] > nums[end]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:  # nums[mid] < nums[end]
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


'''
分为4种情况：
    中间的大于后面的：
        目标值在左半部分
        目标值在右半部分
    中间的小于后面的：（数组中不存在重复项，所以没有等于）
        目标值在右半部分
        目标值在左半部分
'''
