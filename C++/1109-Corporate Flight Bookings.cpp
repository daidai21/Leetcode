class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> res(n);
        for (vector<int> v : bookings) {
            res[v[0] - 1] += v[2];
            if (v[1] < n)
                res[v[1]] -= v[2];
        }
        for (int i = 1; i < n; ++i)
            res[i] += res[i - 1];
        return res;
    }
};
