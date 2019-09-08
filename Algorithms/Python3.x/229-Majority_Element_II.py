# Runtime: 136 ms, faster than 74.29% of Python3 online submissions for Majority Element II.
# Memory Usage: 15.1 MB, less than 5.88% of Python3 online submissions for Majority Element II.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                count1, candidate1 = 1, num
            elif count2 == 0:
                count2, candidate2 = 1, num
            else:
                count1 -= 1
                count2 -= 1
        return [num for num in (candidate1, candidate2) if nums.count(num) > len(nums) // 3]
