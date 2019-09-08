// Runtime: 48 ms, faster than 98.45% of C++ online submissions for Task Scheduler.
// Memory Usage: 9.6 MB, less than 100.00% of C++ online submissions for Task Scheduler.
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> temp(26, 0);
        for (char ch : tasks)
            ++temp[ch - 'A'];
        sort(temp.begin(), temp.end());
        int i = 25;
        while (i > 0 && temp[i] == temp[25])
            --i;
        return max((int) tasks.size(), (n + 1) * (temp[25] - 1) + 25 - i);
    }
};
