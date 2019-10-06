class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        return min(sum([chip % 2 for chip in chips]), sum([not chip % 2 for chip in chips]))
