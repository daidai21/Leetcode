// Runtime: 8 ms, faster than 79.56% of C++ online submissions for 3Sum Closest.
// Memory Usage: 8.7 MB, less than 90.57% of C++ online submissions for 3Sum Closest.
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int result = accumulate(nums.begin(), nums.begin() + 3, 0);
        for (int i = 0; i < nums.size(); ++i) {
            int j = i + 1,
                k = nums.size() - 1;
            while (j < k) {
                int three_sum = nums[i] + nums[j] + nums[k];
                if (three_sum == target)
                    return target;
                else if (abs(three_sum - target) < abs(result - target))
                    result = three_sum;
                else if (three_sum > target)
                    --k;
                else if (three_sum < target)
                    ++j;
                else
                    return three_sum;
            }
        }
        return result;
    }
};
