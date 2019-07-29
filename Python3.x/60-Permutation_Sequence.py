# Time Limit Exceeded
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        enumeration = []
        def recursion(cur):
            if len(cur) == n:
                enumeration.append(cur)
            for i in range(1, n + 1):
                if i not in cur:
                    recursion(cur + [i])

        recursion([])
        return "".join(map(str, enumeration[k - 1]))


# Runtime: 36 ms, faster than 75.86% of Python3 online submissions for Permutation Sequence.
# Memory Usage: 13.6 MB, less than 5.03% of Python3 online submissions for Permutation Sequence.
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        res = ""
        k -= 1
        while n > 0:
            n -= 1
            idx, k = divmod(k, math.factorial(n))
            res += str(nums[idx])
            nums.remove(nums[idx])
        return res
