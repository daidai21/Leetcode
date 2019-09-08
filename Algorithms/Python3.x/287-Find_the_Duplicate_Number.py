# sort list
# Runtime: 44 ms, faster than 67.92% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Find the Duplicate Number.
class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        nums.sort()
        for i, item in enumerate(nums):
            if item == nums[i - 1]: return nums[i]


# set
Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Find the Duplicate Number.
class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        docker = set()
        for num in nums:
            if num in docker: return num
            docker.add(num)



# Floyd 龟兔 （循环检测）
# Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Find the Duplicate Number.
class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        slow, fast = nums[0], nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if fast == slow: break
        point_1, point_2 = nums[0], slow
        while point_1 != point_2:
            point_1, point_2 = nums[point_1], nums[point_2]
        return point_1


# 二分查找 鸽笼原理
# Runtime: 64 ms, faster than 27.55% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Find the Duplicate Number.
class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        start, end = 1, len(nums) - 1
        while start <= end:
            mid = int((start + end) / 2)
            tmp = sum(x <= mid for x in nums)
            if tmp > mid: end = mid - 1
            else: start = mid + 1
        return start
