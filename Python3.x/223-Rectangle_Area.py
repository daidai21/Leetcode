# Runtime: 60 ms, faster than 78.54% of Python3 online submissions for Rectangle Area.
# Memory Usage: 14.1 MB, less than 12.50% of Python3 online submissions for Rectangle Area.
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        overlap_width = min(C, G) - max(A, E) if min(C, G) > max(A, E) else 0
        overlap_height = min(D, H) - max(B, F) if min(D, H) > max(B, F) else 0
        return (D - B) * (C - A) - overlap_width * overlap_height + (G - E) * (H - F)


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        return (D - B) * (C - A) - max(0, (min(C, G) - max(A, E))) * max(0, (min(D, H) - max(B, F))) + (G - E) * (H - F)
