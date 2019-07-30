// Runtime: 20 ms, faster than 71.13% of C++ online submissions for Container With Most Water.
// Memory Usage: 9.7 MB, less than 87.35% of C++ online submissions for Container With Most Water.
class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_space = 0, l = 0, r = height.size() - 1;
        while (l < r) {
            max_space = max(max_space, min(height[l], height[r]) * (r - l));
            if (height[l] > height[r])
                --r;
            else
                ++l;
        }
        return max_space;
    }
};