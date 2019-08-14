// Runtime: 36 ms, faster than 5.31% of C++ online submissions for Evaluate Division.
// Memory Usage: 27.8 MB, less than 5.55% of C++ online submissions for Evaluate Division.
class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        map<string, map<string, double>> dic;
        for (int idx = 0; idx < equations.size(); ++idx) {
            string mol = equations[idx][0], den = equations[idx][1]; // molecular and denominator
            dic[mol][mol] = 1.0;
            dic[den][den] = 1.0;
            dic[mol][den] = values[idx];
            dic[den][mol] = 1.0 / values[idx];
        }
        for (auto i : dic)
            for (auto j : dic)
                for (auto k : dic)
                    if (dic[j.first].find(i.first) != dic[j.first].end() && dic[i.first].find(k.first) != dic[i.first].end())
                        dic[j.first][k.first] = dic[j.first][i.first] * dic[i.first][k.first];
        vector<double> result(queries.size());
        for (int idx = 0; idx < queries.size(); ++idx) {
            string mol = queries[idx][0], den = queries[idx][1]; // molecular and denominator
            if (dic.find(mol) != dic.end() && dic[mol].find(den) != dic[mol].end())
                result[idx] = dic[mol][den];
            else
                result[idx] = -1.0;
        }
        return result;
    }
};
