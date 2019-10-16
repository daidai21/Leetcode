// Runtime: 8 ms, faster than 58.83% of C++ online submissions for Trapping Rain Water.
// Memory Usage: 9 MB, less than 93.67% of C++ online submissions for Trapping Rain Water.
// two pointer
class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0, r = height.size() - 1,
            l_max = 0, r_max = 0,
            volume = 0;
        while (l < r) {
            if (height[l] < height[r]) {
                if (height[l] >= l_max)
                    l_max = height[l];
                else
                    volume += l_max - height[l];
                ++l;
            } else {
                if (height[r] >= r_max)
                    r_max = height[r];
                else
                    volume += r_max - height[r];
                --r;
            }
        }
        return volume;
    }
};


// Runtime: 4 ms, faster than 95.80% of C++ online submissions for Trapping Rain Water.
// Memory Usage: 9.1 MB, less than 78.48% of C++ online submissions for Trapping Rain Water.
// dp
class Solution {
public:
    int trap(vector<int>& height) {
        int volume = 0;
        if (!height.size())
            return volume;
        vector<int> right_max(height.size(), 0),
                    left_max(height.size(), 0);
        left_max[0] = height[0];
        for (int i = 1; i < height.size(); ++i)
            left_max[i] = max(left_max[i - 1], height[i]);
        right_max[height.size() - 1] = height[height.size() - 1];
        for (int i = height.size() - 2; i >= 0; --i)
            right_max[i] = max(right_max[i + 1], height[i]);
        for (int i = 1; i < height.size() - 1; ++i)
            volume += min(left_max[i], right_max[i]) - height[i];
        return volume;
    }
};
