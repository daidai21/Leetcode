# Runtime: 748 ms, faster than 6.47% of Python3 online submissions for Range Sum Query - Mutable.
# Memory Usage: 16.6 MB, less than 89.58% of Python3 online submissions for Range Sum Query - Mutable.
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)