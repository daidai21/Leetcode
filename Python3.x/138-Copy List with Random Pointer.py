{
    "$id": "1",
    "next": {
        "$id": "2",
        "next": null,
        "random": {
            "$ref": "2"
        },
        "val": 2
    },
    "random": {
        "$ref": "2"
    },
    "val": 1
}


# Runtime: 36 ms, faster than 99.61% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 15.5 MB, less than 72.46% of Python3 online submissions for Copy List with Random Pointer.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head):
        dic, m, n = {}, head, head
        while m:
            dic[m] = Node(m.val, None, None)
            m = m.next
        while n:
            dic[n].next, dic[n].random = dic.get(n.next), dic.get(n.random)
            n = n.next
        return dic.get(head)


# Runtime: 44 ms, faster than 90.07% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 15.5 MB, less than 64.51% of Python3 online submissions for Copy List with Random Pointer.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head):
        dic = collections.defaultdict(lambda: Node(0, None, None))
        dic[None], n = None, head
        while n:
            dic[n].val, dic[n].next, dic[n].random = n.val, dic[n.next], dic[n.random]
            n = n.next
        return dic[head]
