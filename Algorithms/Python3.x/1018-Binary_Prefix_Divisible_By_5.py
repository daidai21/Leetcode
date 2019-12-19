# Runtime: 320 ms, faster than 64.05% of Python3 online submissions for Binary Prefix Divisible By 5.
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Binary Prefix Divisible By 5.
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        prefix = 0
        result = []
        for a in A:
            prefix = prefix * 2 + a
            if prefix % 5 == 0:
                result.append(True)
            else:
                result.append(False)
        return result
