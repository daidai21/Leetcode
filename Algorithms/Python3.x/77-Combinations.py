# Runtime: 636 ms, faster than 41.83% of Python3 online submissions for Combinations.
# Memory Usage: 15.5 MB, less than 10.40% of Python3 online submissions for Combinations.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def recursion(i, curr):
            if len(curr) == k:
                res.append(curr)
            for i in range(i + 1, n + 1):
                recursion(i, curr + [i])

        recursion(0, [])
        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        elif k == n:
            return [[i for i in range(1, n + 1)]]
        else:
            res = []
            def recursion(i, curr):
                if len(curr) == k:
                    res.append(curr)
                for i in range(i + 1, n + 1):
                    recursion(i, curr + [i])

            recursion(0, [])
            return res


# Runtime: 104 ms, faster than 88.61% of Python3 online submissions for Combinations.
# Memory Usage: 15.5 MB, less than 9.48% of Python3 online submissions for Combinations.
class Solution:
    def combine(self, n, k):
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        elif k == n:
            return [[i for i in range(1, n + 1)]]
        else:
            res = []
            res += self.combine(n-1, k)
            part = self.combine(n - 1, k - 1)
            for ls in part:
                ls.append(n)
            res += part
            return res
