# Runtime: 328 ms, faster than 55.58% of Python3 online submissions for Random Pick Index.
# Memory Usage: 21.5 MB, less than 33.33% of Python3 online submissions for Random Pick Index.
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.val_idx_dic = {}
        for idx, num in enumerate(nums):
            if num in self.val_idx_dic:
                self.val_idx_dic[num].append(idx)
            else:
                self.val_idx_dic[num] = [idx]

    def pick(self, target: int) -> int:
        return random.choice(self.val_idx_dic[target])


# Reservoir Sampling
# Runtime: 316 ms, faster than 71.66% of Python3 online submissions for Random Pick Index.
# Memory Usage: 16.7 MB, less than 33.33% of Python3 online submissions for Random Pick Index.
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


import random


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.len_nums = len(self.nums)

    def pick(self, target: int) -> int:
        n = 0  # the sequence length of target value in self.nums
        res = None
        for idx in range(self.len_nums):
            if self.nums[idx] == target:
                n += 1
                if random.randint(1, n) == n:
                    res = idx
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
