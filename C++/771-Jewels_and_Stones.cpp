// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Jewels and Stones.
// Memory Usage: 8.4 MB, less than 59.15% of C++ online submissions for Jewels and Stones.
class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int res = 0;
        for (char s : S)
            for (char j : J)
                if (s == j)
                    res++;
        return res;
    }
};