# Runtime: 296 ms, faster than 16.39% of Python3 online submissions for LFU Cache.
# Memory Usage: 23.2 MB, less than 50.00% of Python3 online submissions for LFU Cache.
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.frequency = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.__sentinel = Node(None, None)
        self.__sentinel.next = self.__sentinel
        self.__sentinel.prev = self.__sentinel
        self.__size = 0

    def __len__(self):
        return self.__size

    def append(self, node):
        node.next = self.__sentinel.next
        node.prev = self.__sentinel
        node.next.prev = node
        self.__sentinel.next = node
        self.__size += 1

    def pop(self, node=None):
        if self.__size == 0:
            return 
        if not node:
            node = self.__sentinel.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.__size -= 1
        return node


class LFUCache:
    """
    func:
        __update:
            update frequency
            update __min_frequency
    """
    def __init__(self, capacity: int):
        self.__size = 0
        self.__capacity = capacity
        self.__node = dict()
        self.__frequency = collections.defaultdict(DoublyLinkedList)
        self.__min_frequency = 0

    def __update(self, node):
        frequency = node.frequency
        self.__frequency[frequency].pop(node)
        if self.__min_frequency == frequency and not self.__frequency[frequency]:
            self.__min_frequency += 1
        node.frequency += 1
        frequency = node.frequency
        self.__frequency[frequency].append(node)

    def get(self, key: int) -> int:
        if key not in self.__node:
            return -1
        node = self.__node[key]
        self.__update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.__capacity == 0:
            return 
        if key in self.__node:
            node = self.__node[key]
            self.__update(node)
            node.value = value
        else:
            if self.__size == self.__capacity:
                node = self.__frequency[self.__min_frequency].pop()
                del self.__node[node.key]
                self.__size -= 1
            node = Node(key, value)
            self.__node[key] = node
            self.__frequency[1].append(node)
            self.__min_frequency = 1
            self.__size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
