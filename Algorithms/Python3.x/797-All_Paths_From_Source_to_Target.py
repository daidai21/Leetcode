# bfs
# conclude input have not circle
# Runtime: 116 ms, faster than 89.35% of Python3 online submissions for All Paths From Source to Target.
# Memory Usage: 15.1 MB, less than 40.00% of Python3 online submissions for All Paths From Source to Target.
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.paths = []
        target = len(graph) - 1
        self.bfs(graph, target, [0])
        return self.paths

    def bfs(self, graph, target, curr_path):
        if curr_path[-1] == target:
            self.paths.append(curr_path)
        else:
            for node in graph[curr_path[-1]]:
                self.bfs(graph, target, curr_path + [node])
