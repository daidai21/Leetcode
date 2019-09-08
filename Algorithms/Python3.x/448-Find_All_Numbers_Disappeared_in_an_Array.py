# 暴力
# Time Limit Exceeded
class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        result = []
        for n in range(1, len(nums) + 1):
            if n not in nums: result.append(n)
        return result


# 暴力的优化
class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        length, result, nums = len(nums), [], set(nums)
        for n in range(1, length + 1):
            if n not in nums: result.append(n)
        return result


# 一行
# Runtime: 136 ms, faster than 97.07% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 22.3 MB, less than 22.42% of Python3 online submissions for Find All Numbers Disappeared in an Array.
class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        return list(set(range(1, len(nums) + 1)) - set(nums))


# 正负号标记法
class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        for num in nums:
            index = num if num > 0 else -num
            index -= 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        result = []
        for (index, num) in enumerate(nums):
            if num > 0:
                result.append(index + 1)
        return result


'''
遍历数组nums，记当前元素为n，令nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
再次遍历nums，将正数对应的下标+1返回即为答案，因为正数对应的元素没有被上一步骤标记过
'''


# 正负号标记法
class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        return [i + 1 for i, n in enumerate(nums) if n > 0]
