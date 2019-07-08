class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> backup(nums);
        sort(nums.begin(), nums.end());
        vector<int>::iterator left=nums.begin(), right=nums.end() - 1;
        while(*left + *right != target){
            while(*left + *right < target) left++;
            while(*left + *right > target) right--;
        }
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            if (backup[i] == *left || backup[i] == *right) result.push_back(i);
        }
        return result;
    }
};
