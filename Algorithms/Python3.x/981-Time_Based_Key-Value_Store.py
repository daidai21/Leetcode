# Runtime: 704 ms, faster than 90.10% of Python3 online submissions for Time Based Key-Value Store.
# Memory Usage: 65.8 MB, less than 20.00% of Python3 online submissions for Time Based Key-Value Store.
class TimeMap:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dic:
            lst = self.dic[key]
            l, r = 0, len(lst) - 1
            if lst[0][1] > timestamp:
                return ""
            elif lst[r][1] <= timestamp:
                return lst[r][0]
            else:
                while l <= r:  # binary search
                    mid = (l + r) // 2
                    if lst[mid][1] == timestamp:
                        return lst[mid][0]
                    elif lst[mid][1] < timestamp:
                        l = mid + 1
                    else:
                        r = mid - 1
                return lst[r][0]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
