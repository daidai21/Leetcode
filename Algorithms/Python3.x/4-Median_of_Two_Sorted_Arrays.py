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

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_1, len_2 = len(nums1), len(nums2)
        if len_1 > len_2:
            nums1, nums2, len_1, len_2 = nums2, nums1, len_2, len_1
        idx_min, idx_max, idx_half = 0, len_1, int((len_1 + len_2 + 1) / 2)
        while idx_min <= idx_max:
            # binary search
            i = int((idx_min + idx_max) / 2)
            j = idx_half - i
            if i < len_1 and nums2[j - 1] > nums1[i]:
                idx_min = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                idx_max = i - 1
            else:
                # judge
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                if (len_1 + len_2) % 2 == 1:
                    return max_of_left
                if i == len_1:
                    min_of_right = nums2[j]
                elif j == len_2:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right) / 2.0
