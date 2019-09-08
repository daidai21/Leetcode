// Runtime: 48 ms, faster than 41.35% of C++ online submissions for Subarray Sum Equals K.
// Memory Usage: 14.5 MB, less than 49.33% of C++ online submissions for Subarray Sum Equals K.
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        map<int, int> dic = {{0, 1}};
        int count = 0, add = 0;
        for (int i = 0; i < nums.size(); ++i) {
            add += nums[i];
            if (dic.find(add - k) != dic.end())
                count += dic[add - k];
            if (dic.find(add) != dic.end())
                ++dic[add];
            else
                dic[add] = 1;
        }
        return count;
    }
};
