// Runtime: 88 ms, faster than 85.35% of C++ online submissions for Random Pick Index.
// Memory Usage: 19 MB, less than 90.00% of C++ online submissions for Random Pick Index.
class Solution {
public:
    Solution(vector<int>& nums) {
        nums_ = nums;
    }
    
    int pick(int target) {
        int n = 0;
        int res = -1;
        for (int i = 0; i < nums_.size(); ++i) {
            if (nums_[i] == target) {
                n++;
                if (n == 0)
                    res = i;
                else if (rand() % n == 0)
                    res = i;
            }
        }
        return res;
    }
private:
    vector<int> nums_;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */
