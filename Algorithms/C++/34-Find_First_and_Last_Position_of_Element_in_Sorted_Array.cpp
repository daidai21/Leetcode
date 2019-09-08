# Runtime: 8 ms, faster than 86.80% of C++ online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 10.1 MB, less than 98.57% of C++ online submissions for Find First and Last Position of Element in Sorted Array.
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res = {-1, -1};
        if (nums.size() == 0)
            return res;
        int l = 0, r = nums.size() - 1, idx = NULL;
        while (l <= r) { // l and r is region pointer in here
            int mid = (l + r) / 2;
            if (nums[mid] == target) {
                idx = mid;
                break;
            } else if (nums[mid] > target)
                r = mid - 1;
            else
                l = mid + 1;
        }
        if (nums[idx] == target) { // judge find target index
            l = idx;
            r = idx;
            while (l > 0)
                if (target == nums[l - 1])
                    --l;
                else
                    break;
            while (r < nums.size() - 1)
                if (target == nums[r + 1])
                    ++r;
                else
                    break;
            res[0] = l;
            res[1] = r;
        }
        return res;
    }
};
