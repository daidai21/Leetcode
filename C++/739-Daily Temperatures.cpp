// Runtime: 188 ms, faster than 90.41% of C++ online submissions for Daily Temperatures.
// Memory Usage: 14.7 MB, less than 100.00% of C++ online submissions for Daily Temperatures.
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> res(T.size());
        for (int i = res.size() - 1; i >= 0; --i) {
            int j = i + 1;
            while (j < T.size() && T[j] <= T[i])
                if (res[j] > 0)
                    j = res[j] + j;
                else
                    j = T.size();
            if (j < T.size())
                res[i] = j - i;
        }
        return res;
    }
};


// optimized
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> res(T.size());
        for (int i = res.size() - 1; i >= 0; --i) {
            int j = i + 1;
            while (j < T.size() && T[j] <= T[i])
                j = res[j] > 0 ? j + res[j] : T.size();
            if (j < T.size())
                res[i] = j - i;
        }
        return res;
    }
};
