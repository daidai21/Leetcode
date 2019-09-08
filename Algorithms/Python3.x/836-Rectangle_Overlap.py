# Runtime: 32 ms, faster than 89.53% of Python3 online submissions for Rectangle Overlap.
# Memory Usage: 13.9 MB, less than 8.33% of Python3 online submissions for Rectangle Overlap.
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]


"""
(left1, right1), (left2, right2)
Meet the requirements of the topic  Equivalent to :
    left1 < x < right1 && left2 < x < right2
    left1 < x < right2 && left2 < x < right1
    left1 < right2 && left2 < right1
"""
