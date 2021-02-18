// Runtime: 5 ms, faster than 94.78% of Java online submissions for Merge Intervals.
// Memory Usage: 41.7 MB, less than 67.51% of Java online submissions for Merge Intervals.
class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) {
            return intervals;
        }
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));
        List<int[]> res = new ArrayList<>();
        int[] tmp = intervals[0];
        res.add(tmp);
        for (int[] interval : intervals) {
            if (interval[0] <= tmp[1]) {
                tmp[1] = Math.max(tmp[1], interval[1]);
            } else {
                tmp = interval;
                res.add(tmp);
            }
        }
        return res.toArray(new int[res.size()][]);
    }
}
