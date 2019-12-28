# Time Limit Exceeded
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        min_high = float("inf")
        min_high_root = []
        # dict edges
        dic_edges = {}
        for start, end in edges:
            if start not in dic_edges:
                dic_edges[start] = [end]
            else:
                dic_edges[start].append(end)
            if end not in dic_edges:
                dic_edges[end] = [start]
            else:
                dic_edges[end].append(start)
        for root in range(n):
            # BFS find depth of tree
            layer_num = 1
            layer = [root]
            visited = set([root])
            while layer:
                next_layer = []
                for node in layer:
                    if node in dic_edges:
                        for next_node in dic_edges[node]:
                            if next_node not in visited:
                                next_layer.append(next_node)
                                visited.add(next_node)
                layer = next_layer
                layer_num += 1
            # update result
            if layer_num < min_high:
                min_high_root = [root]
                min_high = layer_num
            elif layer_num == min_high:
                min_high_root.append(root)
        return min_high_root


"""
Discuss: [Iterative remove leaves Python solution](https://leetcode.com/problems/minimum-height-trees/discuss/76132/Iterative-remove-leaves-Python-solution)
Because there're at most two nodes can be Minimum Height Trees. And all leaves are impossible because such nodes. So we can iterative remove leaves and related edges till we reach 1 or 2.
"""
# Runtime: 884 ms, faster than 9.51% of Python3 online submissions for Minimum Height Trees.
# Memory Usage: 18.9 MB, less than 25.00% of Python3 online submissions for Minimum Height Trees.
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        dic = collections.defaultdict(set)
        for u, v in edges:
            dic[u].add(v)
            dic[v].add(u)
        s = set(range(n))
        while len(s) > 2:
            leaves = set(i for i in s if len(dic[i]) == 1)
            s -= leaves
            for i in leaves:
                for j in dic[i]:
                    dic[j].remove(i)
        return list(s)
