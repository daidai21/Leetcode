# Runtime: 56 ms, faster than 17.58% of Python3 online submissions for Restore IP Addresses.
# Memory Usage: 13.8 MB, less than 5.00% of Python3 online submissions for Restore IP Addresses.
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []
        self.res = []
        self.recursion(s, 0, [])
        return self.res

    def recursion(self, s, idx, curr):
        if idx == len(s) and len(curr) == 4 and curr not in self.res:
            self.res.append(".".join(curr))
            return
        else:
            if idx == len(s):
                return 
            elif s[idx] == '0':
                self.recursion(s, idx + 1, curr + [s[idx]])
            else:
                for i in range(idx + 1, len(s) + 1):
                    if 0 <= int(s[idx:i]) <= 255:
                        self.recursion(s, i, curr + [s[idx:i]])


# Runtime: 40 ms, faster than 77.73% of Python3 online submissions for Restore IP Addresses.
# Memory Usage: 13.9 MB, less than 5.00% of Python3 online submissions for Restore IP Addresses.
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []
        self.res = []
        self.dfs(s, 0, "")
        return self.res

    def dfs(self, s, idx, path):
        if idx == 4:
            if not s:
                self.res.append(path[:-1])
            return 
        else:
            for i in range(1, 4):
                if i <= len(s):
                    if i == 1:
                        self.dfs(s[i:], idx + 1, path + s[:i] + '.')
                    elif i == 2 and s[0] != '0':
                        self.dfs(s[i:], idx + 1, path + s[:i] + '.')
                    elif i == 3 and s[0] != '0' and int(s[:3]) <= 255:
                        self.dfs(s[i:], idx + 1, path + s[:i] + '.')
