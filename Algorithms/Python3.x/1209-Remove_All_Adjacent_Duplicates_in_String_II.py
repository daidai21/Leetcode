# Runtime: 76 ms, faster than 100.00% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
# Memory Usage: 15.5 MB, less than 100.00% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)
