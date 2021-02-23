// Runtime: 18 ms, faster than 88.47% of Java online submissions for 3Sum.
// Memory Usage: 42.5 MB, less than 93.49% of Java online submissions for 3Sum.
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for (int left = 0; left < nums.length - 2; ++left) {
            int center = left + 1;
            int right = nums.length - 1;
            int target = -nums[left];
            while (center < right) {
                int sum_2 = nums[center] + nums[right];
                if (target == sum_2) {
                    res.add(Arrays.asList(nums[left], nums[center], nums[right]));
                    while (center < right && nums[center] == nums[center + 1]) center++;
                    while (center < right && nums[right] == nums[right - 1]) right--;
                    center++;
                    right--;
                } else if (sum_2 > target) --right;
                else ++center;
            }
            // del repeat
            while (left < nums.length - 1 && nums[left] == nums[left + 1]) {
                ++left;
            }
        }
        return res;
    }
}
