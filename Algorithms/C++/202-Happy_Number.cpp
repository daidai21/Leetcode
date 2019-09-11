// Runtime: 4 ms, faster than 66.56% of C++ online submissions for Happy Number.
// Memory Usage: 8.7 MB, less than 34.61% of C++ online submissions for Happy Number.
class Solution {
public:
    bool isHappy(int n) {
        set<int> mem;
        while (n != 1) {
            string s = to_string(n);
            int new_n = 0;
            for (char c : s)
                new_n += ((int)c - 48) * ((int)c - 48);
            if (mem.find(new_n) != mem.end())
                return false;
            else
                mem.insert(n);
            n = new_n;
        }
        return true;
    }
};
