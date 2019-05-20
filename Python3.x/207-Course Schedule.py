# 判断是否能形成有向无环图  考察：拓扑排序 dfs / bfs
# dfs
class Solution:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i] == -1: return False
            if visit[i] == 1: return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# if node v has not been visited, then mark it as 0.
# if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
# if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.


# 上边的优化
# Runtime: 36 ms, faster than 99.93% of Python3 online submissions for Course Schedule.
# Memory Usage: 16.1 MB, less than 37.24% of Python3 online submissions for Course Schedule.
class Solution:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visit[i] == -1: return False  # 已经访问，环
            if visit[i] == 1: return True  # 已经访问，非环
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j): return False  # 找环
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i): return False  # 找环
        return True


# 拓扑排序
# Runtime: 44 ms, faster than 97.51% of Python3 online submissions for Course Schedule.
# Memory Usage: 14.3 MB, less than 78.21% of Python3 online submissions for Course Schedule.
class Solution:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        indegree = [0 for i in range(numCourses)]  # 入度
        connection = {i:[] for i in range(numCourses)}  # 连接
        for x, y in prerequisites:  # y指向x的关系
            connection[y].append(x)
            indegree[x] += 1
        zero_indegree = []  # 入度为零的节点
        for i in range(numCourses):
            if indegree[i] == 0:
                zero_indegree.append(i)
        i = 0
        while i < len(zero_indegree):
            for node in connection[zero_indegree[i]]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    zero_indegree.append(node)
            i += 1
        if len(zero_indegree) == numCourses:  # 相等说明图中无环
            return True
        else:
            return False


# 上边的优化
class Solution:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        indegree = [0 for i in range(numCourses)]  # 入度
        connection = {i:[] for i in range(numCourses)}  # 连接
        for x, y in prerequisites:  # y指向x的关系
            connection[y].append(x)
            indegree[x] += 1
        zero_indegree = []  # 入度为零的节点
        for i in range(numCourses):
            if indegree[i] == 0: zero_indegree.append(i)
        i = 0
        while i < len(zero_indegree):
            for node in connection[zero_indegree[i]]:
                indegree[node] -= 1
                if indegree[node] == 0: zero_indegree.append(node)
            i += 1
        return len(zero_indegree) == numCourses  # 相等说明图中无环
