// Runtime: 1 ms, faster than 99.97% of Java online submissions for Minimum Size Subarray Sum.
// Memory Usage: 38.9 MB, less than 65.83% of Java online submissions for Minimum Size Subarray Sum.
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int res = Integer.MAX_VALUE;
        int start = 0;
        int sum = 0;
        for (int end = 0; end < nums.length; ++end) {
            sum += nums[end];
            while (sum >= target) {
                res = Math.min(res, end + 1 - start);
                sum -= nums[start];
                start++;
            }
        }
        return res != Integer.MAX_VALUE ? res : 0;
    }
}
