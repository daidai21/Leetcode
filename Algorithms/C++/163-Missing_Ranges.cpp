class Solution {
public:
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        std::vector<std::string> res;
        for (const int& num : nums) {
            if (num > lower) {
                res.push_back(std::to_string(lower) + (num - 1 > lower ? ("->" + std::to_string(num - 1)) : ""));
            }
            if (num == upper) {
                return res;
            }
            lower = num + 1;
        }
        if (lower <= upper) {
            res.push_back(std::to_string(lower) + (upper > lower ? ("->" + std::to_string(upper)) : "")));
        }
        return res;
    }
}
