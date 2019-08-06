# Runtime: 140 ms, faster than 39.47% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
# Memory Usage: 20.4 MB, less than 5.55% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return self.recursion(values)

    def recursion(self, head):
        if not head:
            return None
        mid = int(len(head) / 2)
        node = TreeNode(head[mid])
        node.left = self.recursion(head[:mid])
        node.right = self.recursion(head[mid + 1:])
        return node


# Runtime: 120 ms, faster than 99.47% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
# Memory Usage: 20.3 MB, less than 5.55% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        length = self.find_len(head)
        def convert(l, r):
            nonlocal head
            if l > r:
                return None
            mid = (l + r) // 2
            left = convert(l, mid - 1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            node.right = convert(mid + 1, r)
            return node

        return convert(0, length - 1)

    def find_len(self, head):
        res = 0
        while head:
            head = head.next
            res += 1
        return res
