# Runtime: 284 ms, faster than 38.56% of Python3 online submissions for Design HashSet.
# Memory Usage: 39.7 MB, less than 7.69% of Python3 online submissions for Design HashSet.
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = [False] * (10 ** 6 + 1)

    def add(self, key: int) -> None:
        self.array[key] = True

    def remove(self, key: int) -> None:
        self.array[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.array[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
