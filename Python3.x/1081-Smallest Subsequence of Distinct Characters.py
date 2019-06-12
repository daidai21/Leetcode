# Runtime: 40 ms, faster than 60.86% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last = {c : i for i, c in enumerate(text)}
        stack = []
        for i, c in enumerate(text):
            if c in stack:
                continue
            else:
                while stack and stack[-1] > c and last[stack[-1]] > i:
                    stack.pop()
                stack.append(c)
        return "".join(stack)


'''
找到每个字符的最后一个位置
为了结果用stack保持这些字符
循环遍历S
    if 如果当前字符小于stack中的最后一个字符 and 最后一个字符存在于下面的流中 ：
        stack弹出已获得较小的结果
'''
