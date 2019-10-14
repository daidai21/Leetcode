// Runtime: 4 ms, faster than 96.53% of C++ online submissions for Fizz Buzz.
// Memory Usage: 9.8 MB, less than 86.67% of C++ online submissions for Fizz Buzz.
class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> res(n, "");
        for (int i = 1; i <= n; ++i) {
            string tmp;
            if (i % 3 == 0)
                tmp = "Fizz";
            if (i % 5 == 0)
                tmp += "Buzz";
            if (tmp == "")
                tmp = to_string(i);
            res[i - 1] = tmp;
        }
        return res;
    }
};
