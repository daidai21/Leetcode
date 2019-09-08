# Runtime: 48 ms, faster than 66.01% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res, n = 0, len(arr)
        stack = [float("inf")]
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res

