# Runtime: 84 ms, faster than 5.74% of Python3 online submissions for Decompress Run-Length Encoded List.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Decompress Run-Length Encoded List.
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for idx in range(0, len(nums), 2):
            for _ in range(nums[idx]):
                res.append(nums[idx + 1])
        return res
