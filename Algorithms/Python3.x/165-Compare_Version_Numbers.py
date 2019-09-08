# Runtime: 36 ms, faster than 68.11% of Python3 online submissions for Compare Version Numbers.
# Memory Usage: 14.1 MB, less than 8.33% of Python3 online submissions for Compare Version Numbers.
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        for i in range(max(len(version1), len(version2))):
            v1, v2 = 0, 0
            if i < len(version1):
                v1 = int(version1[i])
            if i < len(version2):
                v2 = int(version2[i])
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
