# Runtime: 40 ms, faster than 81.69% of Python3 online submissions for Split Array Largest Sum.
# Memory Usage: 13.9 MB, less than 16.67% of Python3 online submissions for Split Array Largest Sum.
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if m == 1:
            return sum(nums)
        elif m == len(nums):
            return max(nums)
        else:
            low, high = max(nums), sum(nums)
            while low < high:
                mid = (low + high) // 2
                if self.valid(nums, m, mid):
                    high = mid
                else:
                    low = mid + 1
            return high

    def valid(self, nums, m, max_val):
        curr = 0
        count = 1
        for num in nums:
            curr += num
            if curr > max_val:
                curr = num
                count += 1
                if count > m:
                    return False
        return True
