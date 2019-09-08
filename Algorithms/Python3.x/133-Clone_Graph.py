"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.cloned = {}
        return self.dfs(node)

    def dfs(self, node):
        if not node:
            return 
        if node in self.cloned:
            return self.cloned[node]
        node_copy = Node(node.val, [])
        self.cloned[node] = node_copy
        for n in node.neighbors:
            n_copy = self.dfs(n)
            if n_copy:
                node_copy.neighbors.append(n_copy)
        return node_copy
