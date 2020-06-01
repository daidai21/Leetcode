// Runtime: 40 ms, faster than 47.66% of C++ online submissions for How Many Numbers Are Smaller Than the Current Number.
// Memory Usage: 10.4 MB, less than 100.00% of C++ online submissions for How Many Numbers Are Smaller Than the Current Number.
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> res;
        for (int i = 0; i< nums.size(); ++i) {
            int cur = nums[i],
                smaller_num = 0;
            for (int j = 0; j < nums.size(); ++j) {
                if (cur > nums[j]) {
                    smaller_num++;
                }
            }
            res.push_back(smaller_num);
        }
        return res;
    }
};
