# Runtime: 40 ms, faster than 60.44% of Python3 online submissions for Simplify Path.
# Memory Usage: 13.8 MB, less than 5.11% of Python3 online submissions for Simplify Path.
class Solution:
    def simplifyPath(self, path: str) -> str:
        tmp = [ch for ch in path.split('/') if ch not in ['', '.']]
        stack = []
        for ch in tmp:
            if ch != "..":
                stack.append(ch)
            elif len(stack) > 0:
                stack.pop()
        return '/' + '/'.join(stack)


# Runtime: 32 ms, faster than 96.70% of Python3 online submissions for Simplify Path.
# Memory Usage: 13.9 MB, less than 5.11% of Python3 online submissions for Simplify Path.
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for tmp in path.split('/'):
            if tmp == "..":
                if len(stack) > 0:
                    stack.pop()
            elif tmp != '' and tmp != '.':
                stack.append(tmp)
        return '/' + '/'.join(stack)
