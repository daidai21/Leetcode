# Runtime: 268 ms, faster than 18.17% of Python3 online submissions for N-Repeated Element in Size 2N Array.
# Memory Usage: 15.1 MB, less than 6.12% of Python3 online submissions for N-Repeated Element in Size 2N Array.
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        repeat_num = len(A) // 2
        mem = {}
        for a in A:
            mem[a] = mem[a] + 1 if a in mem else 1
        for k, v in mem.items():
            if v == repeat_num:
                return k


# Runtime: 240 ms, faster than 75.80% of Python3 online submissions for N-Repeated Element in Size 2N Array.
# Memory Usage: 15.1 MB, less than 6.12% of Python3 online submissions for N-Repeated Element in Size 2N Array.
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        seen = set()
        repeat_num = len(A) // 2
        for a in A:
            if a not in seen:
                if A.count(a) == repeat_num:
                    return a
                else:
                    seen.add(a)
