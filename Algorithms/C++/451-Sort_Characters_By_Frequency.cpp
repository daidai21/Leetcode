// Runtime: 40 ms, faster than 16.73% of C++ online submissions for Sort Characters By Frequency.
// Memory Usage: 10.2 MB, less than 100.00% of C++ online submissions for Sort Characters By Frequency.
class Solution {
public:
    string frequencySort(string s) {
        unsigned int counts[256] = {0};
        for (char ch : s)
            ++counts[ch];
        sort(s.begin(), s.end(), [&] (char a, char b) {
            return counts[a] > counts[b] || (counts[a] == counts[b] && a < b);
        });
        return s;
    }
};
