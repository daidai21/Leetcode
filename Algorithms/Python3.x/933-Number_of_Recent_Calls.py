# Time Limit Exceeded
class RecentCounter:
    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        self.times.append(t)
        return len([i for i in self.times if t - 3000 <= i <= t])


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# Time Limit Exceeded
class RecentCounter:
    def __init__(self):
        self.times = []
        self.len_times = 0

    def ping(self, t: int) -> int:
        self.times.append(t)
        self.len_times += 1
        pings = 0
        i = self.len_times - 1
        while i >= 0 and self.times[i] >= t - 3000:
            pings += 1
            i -= 1
        return pings


# queue
# Runtime: 348 ms, faster than 42.88% of Python3 online submissions for Number of Recent Calls.
# Memory Usage: 18.4 MB, less than 20.00% of Python3 online submissions for Number of Recent Calls.
class RecentCounter:
    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        self.times.append(t)
        while self.times[0] < t - 3000:
            self.times.pop(0)
        return len(self.times)
