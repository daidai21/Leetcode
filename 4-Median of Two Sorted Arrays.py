class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x, y, i = 0, 0, 0
        big = []
        while x < len(nums1) and y < len(nums2):
            if nums1[x] <= nums2[y]:
                big.append(nums1[x])
                x, i = x + 1, i + 1
            else:
                big.append(nums2[y])
                y, i = y + 1, i + 1
        while x < len(nums1):
            big.append(nums1[x])
            i, x = i + 1, x + 1
        while y < len(nums2):
            big.append(nums2[y])
            i, y = i + 1, y + 1
        if len(big) % 2 == 1:
            return big[int(len(big) / 2)]
        else:
            return (big[int(len(big) / 2)] + big[int(len(big) / 2 - 1)]) / 2


'''
常规操作
将两个数组排序合并
然后计算合并后数组的中位数
'''