# Math: Manhattan distance
# Runtime: 48 ms, faster than 76.63% of Python3 online submissions for Escape The Ghosts.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Escape The Ghosts.
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        self_dist = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            if abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) <= self_dist:
                return False
        return True
