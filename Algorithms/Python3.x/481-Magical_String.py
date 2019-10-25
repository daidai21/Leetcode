# Runtime: 1396 ms, faster than 5.38% of Python3 online submissions for Magical String.
# Memory Usage: 15 MB, less than 25.00% of Python3 online submissions for Magical String.
class Solution:
    def magicalString(self, n: int) -> int:
        lst = [1, 2, 2]
        next_ = 1
        res = 0
        idx = 2
        for _ in range(100000):
            val = lst[idx]
            lst.append(next_)
            if val == 2:
                lst.append(next_)
            idx += 1
            next_ = 1 if next_ == 2 else 2
        for i in range(n):
            res += lst[i] == 1
        return res


# Runtime: 156 ms, faster than 60.22% of Python3 online submissions for Magical String.
# Memory Usage: 14.7 MB, less than 25.00% of Python3 online submissions for Magical String.
class Solution:
    def magicalString(self, n: int) -> int:
        lst = [1, 2, 2]
        next_ = 1
        res = 0
        idx = 2
        while len(lst) < n:
            val = lst[idx]
            lst.append(next_)
            if val == 2:
                lst.append(next_)
            idx += 1
            next_ = 1 if next_ == 2 else 2
        for i in range(n):
            res += lst[i] == 1
        return res
