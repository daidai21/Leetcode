# Runtime: 24 ms, faster than 98.00% of Python3 online submissions for Construct the Rectangle.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Construct the Rectangle.
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = int(area ** 0.5)
        while area % W != 0:
            W -= 1
        return [int(area / W), int(W)]
