# Dynamic Programming
# Runtime: 32 ms, faster than 95.08% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.3 MB, less than 14.94% of Python3 online submissions for Pascal's Triangle.
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1 for _ in range(i + 1)]
            if i == 0 or i == 1:  # 只有一行
                pass
            else:
                for col in range(1, i):  # 多列
                    row[col] = res[i - 1][col - 1] + res[i - 1][col]
            res.append(row)
        return res
