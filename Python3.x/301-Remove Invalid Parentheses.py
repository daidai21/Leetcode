# 枚举去除的点，当找到后停止BFS树的扩展（因为要去除最少括号，所以即使有其他的结果，也一定在同一层）
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s: return [""]
        q = {s}
        while q:
            ans = list(filter(self.is_valid_parenthese, q))
            if ans: return ans
            q = {cur[:i] + cur[i + 1:] for cur in q for i, _ in enumerate(cur)}

    def is_valid_parenthese(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0:
                    return False
                cnt -= 1
        return cnt == 0
