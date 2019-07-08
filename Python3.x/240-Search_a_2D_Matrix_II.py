# Runtime: 48 ms, faster than 95.33% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 17.1 MB, less than 100.00% of Python3 online submissions for Search a 2D Matrix II.
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []: return False
        row, col, width = len(matrix) - 1, 0, len(matrix[0])
        while row >= 0 and col < width:
            if matrix[row][col] == target: return True
            elif matrix[row][col] > target: row -= 1
            else: col += 1
        return False


'''
先搜索定位到行，再搜索到列
'''


# 暴力
# Runtime: 52 ms, faster than 59.51% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 16.9 MB, less than 100.00% of Python3 online submissions for Search a 2D Matrix II.
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for line in matrix:
            for item in line:
                if item == target: return True
        return False
