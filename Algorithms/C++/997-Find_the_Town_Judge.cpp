class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        vector<int> count(N + 1);
        for (vector<int> tmp : trust) {
            count[tmp[0]]--;
            count[tmp[1]]++;
        }
        for (int i = 1; i <= N; ++i) {
            if (count[i] == N - 1)
                return i;
        }
        return -1;
    }
};
