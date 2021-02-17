// 每个while循环添加四个方向的行，一层一层的添加
// Runtime: 0 ms, faster than 100.00% of Java online submissions for Spiral Matrix.
// Memory Usage: 37.3 MB, less than 49.77% of Java online submissions for Spiral Matrix.
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<>();
        if (matrix.length == 0)
            return ans;
        int r1 = 0, r2 = matrix.length - 1;
        int c1 = 0, c2 = matrix[0].length - 1;
        while (r1 <= r2 && c1 <= c2) {
            for (int c = c1; c <= c2; ++c) ans.add(matrix[r1][c]);
            for (int r = r1 + 1; r <= r2; ++r) ans.add(matrix[r][c2]);
            if (r1 < r2 && c1 < c2) {
                for (int c = c2 - 1; c > c1; --c) ans.add(matrix[r2][c]);
                for (int r = r2; r > r1; --r) ans.add(matrix[r][c1]);
            }
            r1++;
            r2--;
            c1++;
            c2--;
        }
        return ans;
    }
}
