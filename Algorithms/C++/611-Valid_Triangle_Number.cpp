// Time Limit Exceeded
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int count = 0;
        for (int i = 0; i + 2 < nums.size(); ++i)
            for (int j = i + 1; j + 1 < nums.size(); ++j)
                for (int k = j + 1; k < nums.size(); ++k)
                    if (nums[i] + nums[j] > nums[k] && nums[i] + nums[k] > nums[j] && nums[j] + nums[k] > nums[i])
                        count++;
        return count;
    }
};
