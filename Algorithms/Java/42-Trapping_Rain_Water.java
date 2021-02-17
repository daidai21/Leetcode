// 两个指针往中间扫
// Runtime: 0 ms, faster than 100.00% of Java online submissions for Trapping Rain Water.
// Memory Usage: 39.1 MB, less than 22.50% of Java online submissions for Trapping Rain Water.
class Solution {
    public int trap(int[] height) {
        int left = 0,
            right = height.length - 1;
        int ans = 0;
        int left_max = 0,
            right_max = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= left_max) {
                    left_max = height[left];
                } else {
                    ans += left_max - height[left];
                }
                left++;
            } else {
                if (height[right] >= right_max) {
                    right_max = height[right];
                } else {
                    ans += right_max - height[right];
                }
                right--;
            }
        }
        return ans;
    }
}
