# Runtime: 44 ms, faster than 62.07% of Python3 online submissions for Swap Adjacent in LR String.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Swap Adjacent in LR String.
################################################################################
# brainteaser (two pointer)
# Think of the L and R as people on a horizontal line, where X is people.
################################################################################
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i, j = 0, 0  # start and end point
        while i < len(start) and j < len(end):
            while i + 1 < len(start) and start[i] == 'X':
                i += 1
            while j + 1 < len(end) and end[j] == 'X':
                j += 1
            if start[i] != end[j]:
                return False
            elif start[i] == 'L' and i < j:
                return False
            elif start[i] == 'R' and j < i:
                return False
            i += 1
            j += 1
        return True


print(Solution().canTransform("X","L"))  # false
print(Solution().canTransform("RXXLRXRXL","XRLXXRRLX"))  # true
print(Solution().canTransform("XXRXXLXXXX","XXXXRXXLXX"))  # false
