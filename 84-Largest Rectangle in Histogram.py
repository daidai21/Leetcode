class Solution:
    def largestRectangleArea(self, height):
        max_space = 0
        for i in range(len(height)):
            if i + 1 < len(height) and height[i] <= height[i + 1]: continue
            min_high = height[i]
            for j in range(i, -1, -1):
                min_high = min(min_high, height[j])
                max_space = max(max_space, min_high * (i - j + 1))
        return max_space


'''
借鉴递增的思想，复杂度高度栈的解法
'''


# 单调非递减栈
class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack, max_space = [-1], 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                max_space = max(max_space, h * w)
            stack.append(i)
        return max_space


'''
如果height是升序的，必须1，2，3，那么就是比较（1 * 3）vs（2 * 2）vs（3 * 1），也就是max（height[i] * (len(height) - 1)）

用栈来模拟，遍历heights数组，并比较与栈顶元素stack[-1]的大小：
    大于等于栈顶元素，就push进去；
    小于栈顶元素，持续弹栈，并记录这个高度的最大面积，直至栈为空。然后将弹出的数全部替换为降序点的值，即做到了整体依然是有序非降的。
整个过程中，即把所有的局部最大矩阵计算过了，又在宽度范围内保留了全部的场景。
宽度=当前索引-前索引
'''


# 暴力
# Time Limit Exceeded
class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        max_space = 0
        for left in range(len(heights)):
            for right in range(left, len(heights)):
                high = min(heights[left:right + 1])
                max_space = max(max_space, high * (right - left + 1))
        return max_space
