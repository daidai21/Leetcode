# Runtime: 664 ms, faster than 6.74% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 20.1 MB, less than 5.01% of Python3 online submissions for ZigZag Conversion.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        tmp = [[''] * len(s) for _ in range(numRows)]
        row, col, direction = 0, 0, "down"
        for c in s:
            tmp[row][col] = c
            if direction == "down":
                if row < numRows - 1:
                    row += 1
                else:
                    direction = "up_right"
                    row -= 1
                    col += 1
            elif direction == "up_right":
                if row > 0:
                    row -= 1
                    col += 1
                else:
                    direction = "down"
                    row += 1
        res = ""
        for line in tmp:
            for c in line:
                if c != "":
                    res += c
        return res


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s is None or s == "" or numRows == 1 or numRows >= len(s):
            return s
        res = [''] * numRows
        idx, step = 0, 1
        for c in s:
            res[idx] += c
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
        return ''.join(res)


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        step = (numRows == 1) - 1
        res, idx = [""] * numRows, 0
        for c in s:
            res[idx] += c
            if idx == 0 or idx == numRows - 1:  # change direction
                step = -step
            idx += step
        return ''.join(res)
