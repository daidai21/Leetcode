# Runtime: 88 ms, faster than 11.30% of Python3 online submissions for Robot Return to Origin.
# Memory Usage: 14.1 MB, less than 6.90% of Python3 online submissions for Robot Return to Origin.
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        level, vertical = 0, 0
        for move in moves:
            if move == 'U':
                vertical += 1
            elif move == 'D':
                vertical -= 1
            elif move == 'L':
                level -= 1
            elif move == 'R':
                level += 1
        return level == 0 and vertical == 0


# Runtime: 36 ms, faster than 97.19% of Python3 online submissions for Robot Return to Origin.
# Memory Usage: 14 MB, less than 6.90% of Python3 online submissions for Robot Return to Origin.
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and\
               moves.count('U') == moves.count('D')
