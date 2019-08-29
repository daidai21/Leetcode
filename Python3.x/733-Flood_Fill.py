# Runtime: 108 ms, faster than 6.69% of Python3 online submissions for Flood Fill.
# Memory Usage: 14.1 MB, less than 5.56% of Python3 online submissions for Flood Fill.
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.image = image
        self.dfs(sr, sc, newColor, image[sr][sc])
        return self.image

    def dfs(self, sr, sc, newColor, val):
        if self.image[sr][sc] == val:
            self.image[sr][sc] = newColor
            if sr > 0:
                self.dfs(sr - 1, sc, newColor, val)
            if sr < len(self.image) - 1:
                self.dfs(sr + 1, sc, newColor, val)
            if sc > 0:
                self.dfs(sr, sc - 1, newColor, val)
            if sc < len(self.image[0]) - 1:
                self.dfs(sr, sc + 1, newColor, val)
