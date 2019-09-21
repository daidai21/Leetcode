# Runtime: 180 ms, faster than 21.45% of Python3 online submissions for Construct Quad Tree.
# Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Construct Quad Tree.
# """
# # Definition for a QuadTree node.
# class Node:
#     def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight
# """
# class Solution:
#     def construct(self, grid: List[List[int]]) -> 'Node':
#         if len(grid) == 1:
#             return Node(grid[0][0] == 1, True, None, None, None, None)
#         else:
#             half_len = len(grid) // 2
#             tl = self.construct([elem[:half_len] for elem in grid[:half_len]])
#             tr = self.construct([elem[half_len:] for elem in grid[:half_len]])
#             dl = self.construct([elem[:half_len] for elem in grid[half_len:]])
#             dr = self.construct([elem[half_len:] for elem in grid[half_len:]])
#             if tl.val == tr.val == dl.val == dr.val and tl.isLeaf and tr.isLeaf and dl.isLeaf and dr.isLeaf:
#                 return Node(tl.val, True, None, None, None, None)
#             else:
#                 return Node(True, False, tl, tr, dl, dr)

class Solution(object):
    def construct(self, grid):
        if not grid:
            return None
        elif self.isLeaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)
        else:
            half = len(grid) // 2
            return Node('*',
                        False,
                        self.construct([row[:half] for row in grid[:half]]),
                        self.construct([row[half:] for row in grid[:half]]),
                        self.construct([row[:half] for row in grid[half:]]),
                        self.construct([row[half:] for row in grid[half:]]))

    def isLeaf(self, grid):
        return all(grid[i][j] == grid[0][0] for i in range(len(grid)) for j in range(len(grid[i])))
