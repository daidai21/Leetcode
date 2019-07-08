// 拓扑排序+bfs
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<unordered_set<int>> matrix(numCourses);
        for (int i = 0; i < prerequisites.size(); ++i)
            matrix[prerequisites[i][1]].insert(prerequisites[i][0]);
        vector<int> indegrees(numCourses, 0);
        for (int i = 0; i < numCourses; ++i)
            for (auto it = matrix[i].begin(); it != matrix[i].end(); ++it)
                ++indegrees[*it];
        for (int j = 0, i; j < numCourses; ++j) {
            for (i = 0; i < numCourses && indegrees[i] != 0; ++i);
            if (i == numCourses)
                return false;
            indegrees[i] = -1;
            for (auto it = matrix[i].begin(); it != matrix[i].end(); ++it)
                --indegrees[*it];
        }
        return true;
    }
};


// 拓扑排序+dfs
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>> &prerequisites) {
        vector<unordered_set<int>> matrix(numCourses);
        for (int i = 0; i < prerequisites.size(); ++i)
            matrix[prerequisites[i][1]].insert(prerequisites[i][0]);
        unordered_set<int> visited;
        vector<bool> flag(numCourses, false);
        for (int i = 0; i < numCourses; ++i)
            if (!flag[i])
                if (dfs(matrix, visited, i, flag))
                    return false;
        return true;
    }
private:
    bool dfs(vector<unordered_set<int>> &matrix, unordered_set<int> &visited, int b, vector<bool> &flag) {
        flag[b] = true;
        visited.insert(b);
        for (auto it = matrix[b].begin(); it != matrix[b].end(); ++it)
            if (visited.find(*it) != visited.end() || dfs(matrix, visited, *it, flag))
                return true;
        visited.erase(b);
        return false;
    }
};
