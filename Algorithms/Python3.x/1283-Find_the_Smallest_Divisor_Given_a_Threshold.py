class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            temp = 0
            for num in nums:
                temp += math.ceil(num / mid)
            if threshold >= temp:
                right = mid
            else:
                left = mid + 1
        return left
