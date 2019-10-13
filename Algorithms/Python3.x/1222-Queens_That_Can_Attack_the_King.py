class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # fill to chessboard
        chessboard = [[None] * 8 for _ in range(8)]
        for x, y in queens:
            chessboard[x][y] = 'Q'
        res = []
        king_x, king_y = king[0], king[1]
        # check left
        x, y = king[0], king[1]
        while y >= 0:
            if chessboard[x][y] == 'Q':
                res.append([x, y])
                break
            y -= 1
        # check right
        x, y = king[0], king[1]
        while y < 8:
            if chessboard[x][y] == 'Q':
                res.append([x, y])
                break
            y += 1
        # check up
        x, y = king[0], king[1]
        while x >= 0:
            if chessboard[x][y] == 'Q':
                res.append([x, y])
                break
            x -= 1
        # check down
        x, y = king[0], king[1]
        while x < 8:
            if chessboard[x][y] == 'Q':
                res.append([x, y])
                break
            x += 1
        # check lu
        x, y = king[0], king[1]
        while x >= 0 and y >= 0:
            if chessboard[x][y] == 'Q':
                res.append([x, y])
                break
            x -= 1
            y -= 1
        # check ld
        x, y = king[0], king[1]
        while x >= 0 and y < 8:
            if chessboard[x][y] == 'Q':
                res.append([x, y])
                break
            x -= 1
            y += 1
        # check ru
        x, y = king[0], king[1]
        while x < 8 and y >= 0:
            if chessboard[x][y] == 'Q':
                res.append([x, y])
                break
            x += 1
            y -= 1
        # check rd
        x, y = king[0], king[1]
        while x < 8 and y < 8:
            if chessboard[x][y] == 'Q':
                res.append([x, y])
                break
            x += 1
            y += 1

        return res
