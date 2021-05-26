// Runtime: 0 ms, faster than 100.00% of Java online submissions for Combination Sum III.
// Memory Usage: 36.3 MB, less than 86.89% of Java online submissions for Combination Sum III.
class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result = new ArrayList<>();
        backTracking(result, k, n, 1, new ArrayList<Integer>());
        return result;
    }
    
    private void backTracking(List<List<Integer>> res, int k, int n, int lvl, List<Integer> current) {
        if (n < 0) {
            return ;
        }
        if (n == 0 && k == 0) {
            res.add(new ArrayList<Integer>(current));
        }
        for (int i = lvl; i <= 9; i++) {
            current.add(i);
            backTracking(res, k - 1, n - i, i + 1, current);
            current.remove(current.size() - 1);
        }
    }
}
