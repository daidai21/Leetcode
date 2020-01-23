# Runtime: 152 ms, faster than 7.78% of Python3 online submissions for Reshape the Matrix.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Reshape the Matrix.
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        total_nums = len(nums) * len(nums[0])
        if r * c != total_nums:
            return nums
        que = []
        for line in nums:
            for num in line:
                que.append(num)
        res = []
        for i in range(r):
            row = []
            for j in range(c):
                idx = i * c + j
                row.append(que[idx])
            res.append(row)
        return res
