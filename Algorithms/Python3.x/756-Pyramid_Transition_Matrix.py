# Runtime: 36 ms, faster than 86.46% of Python3 online submissions for Pyramid Transition Matrix.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Pyramid Transition Matrix.
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        graph = collections.defaultdict(lambda: collections.defaultdict(list))
        for a, b, c in allowed:
            graph[a][b].append(c)

        def pyramid(bottom):
            if len(bottom) == 1:
                return True
            for i in itertools.product(*(graph[a][b] for a, b in zip(bottom, bottom[1:]))):
                if pyramid(i):
                    return True
            return False

        return pyramid(bottom)
