class Solution {
public:
    int specialArray(vector<int>& nums) {
        for (int i = 0; i <= 1001; ++i) {
            int cnt = 0;
            for (int j = 0; j < nums.size(); ++j) {
                if (nums[j] >= i) {
                    cnt++;
                }
            }
            if (cnt == i) {
                return cnt;
            }
        }
        return -1;
    }
};
