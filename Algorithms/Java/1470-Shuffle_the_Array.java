// Runtime: 0 ms, faster than 100.00% of Java online submissions for Shuffle the Array.
// Memory Usage: 39.2 MB, less than 98.42% of Java online submissions for Shuffle the Array.
class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] result = new int[2 * n];
        for(int i = 0; i < nums.length; i++) {
            result[i] = i % 2 == 0 ? nums[i / 2] : nums[n + i / 2];
        }
        return result;
    }
}
