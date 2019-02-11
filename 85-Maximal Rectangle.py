# 暴力
# time: 10352 ms, faster than 0.91%
# space: 7.6 MB, less than 93.80%
class Solution:
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix: return 0
        max_space = 0
        # 转化为行高度
        for col in range(len(matrix[0])):
            matrix[0][col] = 1 if matrix[0][col] == "1" else 0
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] = matrix[row - 1][col] + 1 if matrix[row][col] == "1" else 0
        # 计算max_space
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if int(matrix[row][col]) > 0:
                    if max_space == 0: max_space = 1
                    left = col
                    while left > 0:
                        max_space = max(max_space, min(matrix[row][left:col + 1]) * (col - left + 1))
                        left -= 1
                    max_space = max(max_space, min(matrix[row][left:col + 1]) * (col - left + 1))  # 考虑left到0的情况
        return max_space


# 暴力的优化
# time: 9340 ms, faster than 0.91%
# space: 7.6 MB, less than 44.57%
class Solution:
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        if not matrix: return 0
        max_space = 0
        for col in range(len(matrix[0])): matrix[0][col] = int(matrix[0][col])
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] = matrix[row - 1][col] + 1 if matrix[row][col] == "1" else 0
        # 计算max_space
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if int(matrix[row][col]) > 0:
                    if max_space == 0: max_space = 1
                    left = col
                    while left > 0:
                        max_space = max(max_space, min(matrix[row][left:col + 1]) * (col - left + 1))
                        left -= 1
                    max_space = max(max_space, min(matrix[row][left:col + 1]) * (col - left + 1))
        return max_space


# 栈 要借鉴84题的思想
# time: 76 ms, faster than 99.32%
# space: 7.6 MB, less than 63.18%
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix: return 0
        height = [0] * (len(matrix[0]) + 1)
        ans = 0
        for row in matrix:
            for i in range(len(matrix[0])):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(len(matrix[0]) + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans


'''
[["1","0","1","0","0"]
 ["1","0","1","1","1"]
 ["1","1","1","1","1"]
 ["1","0","0","1","0"]]
首先可以转化为
    第一行，对应的高度为 1 0 1 0 0
    第二行，对应的高度为 2 0 2 1 1
    第三行，对应的高度为 3 1 3 2 2
    第四行，对应的高度为 4 0 0 3 0
其实就是，对于每一行，如果它为1，就加上上一行的高度，否则高度就为0，求得高度以后
使用84题的方法求得面积
'''
