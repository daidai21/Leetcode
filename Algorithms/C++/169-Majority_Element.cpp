// Runtime: 28 ms, faster than 26.89% of C++ online submissions for Majority Element.
// Memory Usage: 11 MB, less than 93.94% of C++ online submissions for Majority Element.
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums[nums.size() / 2];
    }
};


// Runtime: 16 ms, faster than 96.74% of C++ online submissions for Majority Element.
// Memory Usage: 11 MB, less than 96.97% of C++ online submissions for Majority Element.
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int res = nums[0], times = 1;
        for (int i = 1; i < nums.size(); ++i) {
            if (res == nums[i])
                ++times;
            else if (times > 0)
                --times;
            else
                res = nums[i];
        }
        return res;
    }
};
