# Runtime: 56 ms, faster than 8.74% of Python3 online submissions for Implement Stack using Queues.
# Memory Usage: 14 MB, less than 20.00% of Python3 online submissions for Implement Stack using Queues.
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.q1:
            return None
        val = self.q1.pop(0)
        while self.q1:
            self.q2.append(val)
            val = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return val

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.q1:
            return None
        val = self.q1.pop(0)
        while self.q1:
            self.q2.append(val)
            val = self.q1.pop(0)
        self.q2.append(val)
        self.q1, self.q2 = self.q2, self.q1
        return val

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not (self.q1 or self.q2)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
