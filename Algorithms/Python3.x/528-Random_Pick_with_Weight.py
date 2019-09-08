# Runtime: 328 ms, faster than 59.61% of Python3 online submissions for Random Pick with Weight.
# Memory Usage: 18.1 MB, less than 6.67% of Python3 online submissions for Random Pick with Weight.
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(w)
        self.s = sum(w)
        for i in range(1, self.n):
            self.w[i] += self.w[i - 1]

    def pickIndex(self) -> int:
        seed = random.randint(1, self.s)
        l, r = 0, self.n - 1
        while l < r:
            mid = (l + r) // 2
            if seed <= self.w[mid]:
                r = mid
            else:
                l = mid + 1
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
