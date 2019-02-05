class Solution:
    def findUnsortedSubarray(self, nums: 'List[int]') -> 'int':
        start, end, length = 0, 0, len(nums)
        nums_sorted = sorted(nums)
        for n in range(length):
            if nums[n] != nums_sorted[n]:
                start = n
                break
        for n in range(length - 1, -1, -1):
            if nums[n] != nums_sorted[n]:
                end = n
                break
        return end - start + 1 if end > start else 0
