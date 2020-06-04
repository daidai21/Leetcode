#include <vector>
using namespace std;


// Ref: https://leetcode.com/problems/patching-array/discuss/78488/Solution-%2B-explanation
// Runtime: 16 ms, faster than 22.61% of C++ online submissions for Patching Array.
// Memory Usage: 11.6 MB, less than 50.00% of C++ online submissions for Patching Array.
class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        long int miss = 1, // pre sum
                 added = 0, // result
                 i = 0;
        while (miss <= n) {
            if (i < nums.size() && nums[i] <= miss) {
                miss += nums[i];
                i++;
            } else {
                miss += miss;
                added++;
            }
        }
        return added;
    }
};
