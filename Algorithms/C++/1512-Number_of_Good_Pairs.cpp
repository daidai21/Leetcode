// Runtime: 4 ms, faster than 59.83% of C++ online submissions for Number of Good Pairs.
// Memory Usage: 7.5 MB, less than 20.20% of C++ online submissions for Number of Good Pairs.
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int res = 0;
        int same_num;
        std::set<int> visited;
        for (int i = 0; i < nums.size(); ++i) {
            if (visited.find(nums[i]) != visited.end()) {
                continue;
            }
            same_num = 1;
            for (int j = i + 1; j < nums.size(); ++j) {
                if (nums[i] == nums[j]) {
                    same_num++;
                }
            }
            if (same_num > 1) {
                int combination = 0;
                for (int k = 2; k <= same_num; ++k) {
                    combination += k - 1;
                }
                res += combination;
            }
            visited.insert(nums[i]);
        }
        return res;
    }
};
