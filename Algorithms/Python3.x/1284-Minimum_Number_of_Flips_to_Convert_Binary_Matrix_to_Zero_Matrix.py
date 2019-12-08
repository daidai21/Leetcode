# Runtime: 160 ms, faster than 33.33% of Python3 online submissions for Minimum Number of Flips to Convert Binary Matrix to Zero Matrix.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Minimum Number of Flips to Convert Binary Matrix to Zero Matrix.
# BFS
from collections import deque
from copy import deepcopy


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        self.len_row = len(mat)
        self.len_col = len(mat[0])
        visited = set()
        queue = deque([[mat, 0]])
        while queue:
            for _ in range(len(queue)):
                tmp_mat, step = queue.popleft()
                if self.valid(tmp_mat):
                    return step
                for row in range(self.len_row):
                    for col in range(self.len_col):
                        tmp_mat_flip = self.flip(tmp_mat, row, col)
                        tmp_mat_flip_str = self.mat_to_str(tmp_mat_flip)
                        if tmp_mat_flip_str in visited:
                            continue
                        else:
                            queue.append([tmp_mat_flip, step + 1])
                            visited.add(tmp_mat_flip_str)
        return -1

    def flip(self, mat, x, y):
        new_mat = deepcopy(mat)
        new_mat[x][y] = 1 - new_mat[x][y]
        for i, j in ((x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)):
            if 0 <= i < self.len_row and 0 <= j < self.len_col:
                new_mat[i][j] = 1 - new_mat[i][j]
        return new_mat

    def valid(self, mat):
        return sum(sum(mat[row]) for row in range(self.len_row)) == 0

    def mat_to_str(self, mat):
        result = ""
        for row in range(self.len_row):
            for col in range(self.len_col):
                result += str(mat[row][col])
        return result
