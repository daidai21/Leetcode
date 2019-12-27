# DFS
# Time Limit Exceeded
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if num == "":
            return []
        self.res = []
        self.dfs(num, "", target)
        return self.res

    def dfs(self, num, cur, target):
        if len(num) == 1:
            cur += num
            if eval(cur) == target:
                self.res.append(cur)
        else:
            cur += num[0]
            for opt in ('+', '-', '*'):
                self.dfs(num[1:], cur + opt, target)
            if cur[-1] != '0':
                self.dfs(num[1:], cur, target)


# dfs
# Runtime: 856 ms, faster than 54.75% of Python3 online submissions for Expression Add Operators.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Expression Add Operators.
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.res = []
        self.target = target
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]))
        return self.res

    def dfs(self, num, tmp, cur, last):
        if not num:
            if cur == self.target:
                self.res.append(tmp)
            return 
        for i in range(1, len(num) + 1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != '0'):
                self.dfs(num[i:], tmp + '+' + val, cur + int(val), int(val))
                self.dfs(num[i:], tmp + '-' + val, cur - int(val), -int(val))
                self.dfs(num[i:], tmp + '*' + val, cur - last + last * int(val), last * int(val))
