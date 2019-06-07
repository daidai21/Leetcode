// 暴力
// 先排序再遍历搜索
// Runtime: 24 ms, faster than 99.23% of C++ online submissions for Contains Duplicate.
// Memory Usage: 11.5 MB, less than 78.15% of C++ online submissions for Contains Duplicate.
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(begin(nums), end(nums));
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] == nums[i - 1])
                return true;
        }
        return false;
    }
};


// set
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> tmp;
        for (int i = 0; i < nums.size(); ++i) {
            if (tmp.find(nums[i]) != tmp.end())
                return true;
            else
                tmp.insert(nums[i]);
        }
        return false;
    }
};


// set
// Runtime: 48 ms, faster than 40.46% of C++ online submissions for Contains Duplicate.
// Memory Usage: 18.3 MB, less than 5.03% of C++ online submissions for Contains Duplicate.
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        return nums.size() > set<int>(nums.begin(), nums.end()).size();
    }
};


// set
// Runtime: 40 ms, faster than 76.39% of C++ online submissions for Contains Duplicate.
// Memory Usage: 16.7 MB, less than 18.05% of C++ online submissions for Contains Duplicate.
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        for (int i : nums) {
            if (++mp[i] > 1)
                return true;
        }
        return false;
    }
};
