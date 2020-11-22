# Runtime: 72 ms, faster than 41.01% of Python3 online submissions for Design Circular Queue.
# Memory Usage: 15 MB, less than 6.69% of Python3 online submissions for Design Circular Queue.
class MyCircularQueue:
    
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.arr = [None] * k
        self.front = 0
        self.rear = -1
        self.len = 0  # filled length

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % len(self.arr)
        self.len += 1
        self.arr[self.rear] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.arr)
        self.len -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if self.isEmpty() else self.arr[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return -1 if self.isEmpty() else self.arr[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.len == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.arr) == self.len


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
