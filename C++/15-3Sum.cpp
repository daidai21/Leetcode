class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        int n = nums.size();
        for (int left = 0; left < n; ++left) {
            int center = left + 1, right = n - 1;
            int target = -nums[left];
            while (center < right) {
                int sum_2 = nums[center] + nums[right];
                if (sum_2 == target) {
                    vector<int> tmp = {nums[left], nums[center], nums[right]};
                    res.push_back(tmp);
                    while (center < right && nums[center] == tmp[1])
                        ++center;
                    while (center < right && nums[right] == tmp[2])
                        --right;
                } else if (sum_2 > target)
                    --right;
                else
                    ++center;
            }
            while (left + 1 < n && nums[left] == nums[left + 1])
                ++left;
        }
        return res;
    }
};
