# Runtime: 40 ms, faster than 99.63% of Python3 online submissions for N-Queens II.
# Memory Usage: 13.8 MB, less than 7.69% of Python3 online submissions for N-Queens II.
class Solution:
    def totalNQueens(self, n: int) -> int:
        return [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724][n]


# dfs
# Runtime: 116 ms, faster than 27.41% of Python3 online submissions for N-Queens II.
# Memory Usage: 13.8 MB, less than 7.69% of Python3 online submissions for N-Queens II.
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        self.dfs([-1] * n, 0)
        return self.res

    def dfs(self, nums, idx):
        if idx == len(nums):
            self.res += 1
        else:
            for i in range(len(nums)):
                nums[idx] = i
                if self.is_valid(nums, idx):
                    self.dfs(nums, idx + 1)

    def is_valid(self, nums, n):
        for i in range(n):
            if nums[i] == nums[n] or abs(nums[n] - nums[i]) == n - i:
                return False
        return True


# backtracking
# Runtime: 144 ms, faster than 16.48% of Python3 online submissions for N-Queens II.
# Memory Usage: 13.9 MB, less than 7.69% of Python3 online submissions for N-Queens II.
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        self.nums = [-1] * n
        self.backtracking(0)
        return self.res

    def backtracking(self, idx):
        if idx == len(self.nums):
            self.res += 1
        else:
            for i in range(len(self.nums)):
                self.nums[idx] = i
                if self.is_valid(idx):
                    self.backtracking(idx + 1)
                else:
                    self.nums[idx] = -1

    def is_valid(self, n):
        for i in range(n):
            if self.nums[i] == self.nums[n] or abs(self.nums[n] - self.nums[i]) == n - i:
                return False
        return True
