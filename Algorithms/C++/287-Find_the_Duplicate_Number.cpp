// Runtime: 12 ms, faster than 73.34% of C++ online submissions for Find the Duplicate Number.
// Memory Usage: 9.9 MB, less than 80.00% of C++ online submissions for Find the Duplicate Number.
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for (int i = 1; i < nums.size(); ++i)
            if (nums[i] == nums[i - 1])
                return nums[i];
        return NULL;
    }
};


// Runtime: 8 ms, faster than 97.66% of C++ online submissions for Find the Duplicate Number.
// Memory Usage: 9.8 MB, less than 100.00% of C++ online submissions for Find the Duplicate Number.
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums[0], fast = nums[0];
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        fast = nums[0]; // not longer fast
        while (fast != slow) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
};
