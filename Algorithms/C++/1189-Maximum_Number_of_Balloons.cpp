// Runtime: 8 ms, faster than 24.78% of C++ online submissions for Maximum Number of Balloons.
// Memory Usage: 8.9 MB, less than 100.00% of C++ online submissions for Maximum Number of Balloons.
class Solution {
public:
    int maxNumberOfBalloons(string text) {
        map<char, int> dic = {
            {'b', 0},  // 1
            {'a', 0},  // 1
            {'l', 0},  // 2
            {'o', 0},  // 2
            {'n', 0},  // 1
        };
        for (char ch : text)
            if (dic.find(ch) != dic.end())
                ++dic[ch];
        return min(dic['b'], min(dic['a'], min(dic['l'] / 2, min(dic['o'] / 2, dic['n']))));
    }
};
