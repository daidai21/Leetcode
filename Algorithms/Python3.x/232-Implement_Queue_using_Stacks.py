# Runtime: 36 ms, faster than 64.99% of Python3 online submissions for Implement Queue using Stacks.
# Memory Usage: 13.7 MB, less than 10.00% of Python3 online submissions for Implement Queue using Stacks.
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l1 = []
        self.l2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.l1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.l2 and not self.l1:
            return None
        if not self.l2:
            while self.l1:
                self.l2.append(self.l1.pop())
        return self.l2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.l2:
            return self.l2[-1]
        elif self.l1:
            return self.l1[0]
        else:
            return None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.l1 or self.l2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()