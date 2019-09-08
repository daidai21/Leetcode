# 暴力 穷举
# Runtime: 160 ms, faster than 23.90% of Python3 online submissions for Letter Tile Possibilities.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Letter Tile Possibilities.
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.set_ = set()
        self.recursion('', tiles)
        set_ = list(self.set_)
        return len(set_) - set_.count('')

    def recursion(self, curr, tiles_):
        for i, val in enumerate(tiles_):
            self.set_.add(curr)
            self.recursion(val + curr, tiles_[:i] + tiles_[i + 1:])
        if tiles_ == '':
            self.set_.add(curr)
            return 
