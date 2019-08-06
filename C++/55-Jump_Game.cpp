// Runtime: 12 ms, faster than 72.98% of C++ online submissions for Jump Game.
// Memory Usage: 9.8 MB, less than 99.48% of C++ online submissions for Jump Game.
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int max_ = 0;
        for (int i = 0; i <= max_; ++i) {
            max_ = max(max_, i + nums[i]);
            if (max_ >= nums.size() - 1)
                return true;
        }
        return false;
    }
};
