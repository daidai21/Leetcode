# Runtime: 60 ms, faster than 84.68% of Python3 online submissions for Third Maximum Number.
# Memory Usage: 15 MB, less than 7.69% of Python3 online submissions for Third Maximum Number.
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if not nums:
            return None
        elif len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)


# Runtime: 64 ms, faster than 59.58% of Python3 online submissions for Third Maximum Number.
# Memory Usage: 14.5 MB, less than 7.69% of Python3 online submissions for Third Maximum Number.
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n1 = n2 = n3 = float("-inf")  # from big to small
        for num in nums:
            if num > n1:
                n1, n2, n3 = num, n1, n2
            elif n1 > num > n2:
                n2, n3 = num, n2
            elif n2 > num > n3:
                n3 = num
        return n3 if n3 != float("-inf") else n1
