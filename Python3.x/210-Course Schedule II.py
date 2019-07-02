# Runtime: 44 ms, faster than 97.82% of Python3 online submissions for Course Schedule II.
# Memory Usage: 14.7 MB, less than 54.66% of Python3 online submissions for Course Schedule II.
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(int)
        suc = defaultdict(list)
        for a, b in prerequisites:
            pre[a] += 1
            suc[b].append(a)
        free = set(range(numCourses)) - set(pre)
        out = []
        while free:
            a = free.pop()
            out.append(a)
            for b in suc[a]:
                pre[b] -= 1
                pre[b] or free.add(b)
        return out * (len(out) == numCourses)
