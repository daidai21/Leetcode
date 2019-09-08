# Runtime: 36 ms, faster than 70.02% of Python3 online submissions for Pascal's Triangle II.
# Memory Usage: 13.8 MB, less than 5.08% of Python3 online submissions for Pascal's Triangle II.
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            res.append(1)
            res = [1] + [res[j] + res[j - 1] for j in range(1, i + 1)] + [1]
        return res


# Runtime: 32 ms, faster than 91.21% of Python3 online submissions for Pascal's Triangle II.
# Memory Usage: 13.9 MB, less than 5.08% of Python3 online submissions for Pascal's Triangle II.
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row
