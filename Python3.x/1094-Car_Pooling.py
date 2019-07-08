class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tmp = [0] * 1000
        for n, start, end in trips:
            for i in range(start, end):
                tmp[i] += n
        return max(tmp) <= capacity


# Runtime: 32 ms, faster than 99.05% of Python3 online submissions for Car Pooling.
# Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Car Pooling.
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        for _, n in sorted(x for n, start, end in trips for x in [[start, n], [end, -n]]):
            capacity -= n
            if capacity < 0:
                return False
        return True