# Runtime: 24 ms, faster than 98.62% of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 13.9 MB, less than 49.24% of Python3 online submissions for Create Target Array in the Given Order.
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            if index[i] >= len(target):
                target.append(nums[i])
            else:
                target = target[:index[i]] + [nums[i]] + target[index[i]:]
        return target
