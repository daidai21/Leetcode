# Runtime: 1268 ms, faster than 10.89% of Python3 online submissions for Range Sum Query - Immutable.
# Memory Usage: 17.2 MB, less than 10.00% of Python3 online submissions for Range Sum Query - Immutable.
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)




# Runtime: 92 ms, faster than 78.87% of Python3 online submissions for Range Sum Query - Immutable.
# Memory Usage: 17.4 MB, less than 10.00% of Python3 online submissions for Range Sum Query - Immutable.
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0]
        for num in nums:
            self.nums.append(self.nums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j + 1] - self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)