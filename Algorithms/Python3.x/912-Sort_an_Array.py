# Runtime: 164 ms, faster than 81.24% of Python3 online submissions for Sort an Array.
# Memory Usage: 19.5 MB, less than 85.71% of Python3 online submissions for Sort an Array.
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)


# 超出时间限制
# 看论坛都是超时的
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import random

        def quickSort(l, r):
            if l >= r:
                return
            mid = random.randint(l, r) 
            nums[mid], nums[l] = nums[l], nums[mid]

            tmpVal = nums[l]
            p1, p2 = l, r
            while p1 < p2:
                while p1 < p2 and nums[p2] >= tmpVal:
                    p2 -= 1
                nums[p1] = nums[p2]

                while p1 < p2 and nums[p1] <= tmpVal:
                    p1 += 1
                nums[p2] = nums[p1]
            nums[p1] = tmpVal
            
            quickSort(l, p1 - 1)
            quickSort(p1 + 1, r)

        nums = nums
        quickSort(0, len(nums) - 1)
        return nums

