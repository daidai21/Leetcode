# Runtime: 244 ms, faster than 5.58% of Python3 online submissions for Linked List Random Node.
# Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for Linked List Random Node.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        if self.head is None:
            return -1
        n = 0  # length of list visited
        cur = self.head
        res = cur.val
        while cur:
            if random.randint(0, n) == n:
                res = cur.val
            cur = cur.next
            n += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
