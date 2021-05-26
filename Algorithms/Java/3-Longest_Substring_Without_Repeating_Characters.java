class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] mp = new int[128];
        int l = 0, r = 0, res = 0;
        while (r < s.length()) {
            mp[s.charAt(r)]++;
            while (mp[s.charAt(r)] > 1) {
                mp[s.charAt(l)]--;
                l++;
            }
            res = Math.max(res, r - l + 1);
            r++;
        }
        return res;
    }
}
