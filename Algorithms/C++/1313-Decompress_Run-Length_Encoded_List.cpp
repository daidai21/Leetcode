// Runtime: 52 ms, faster than 11.52% of C++ online submissions for Decompress Run-Length Encoded List.
// Memory Usage: 10.7 MB, less than 100.00% of C++ online submissions for Decompress Run-Length Encoded List.
class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> res;
        for (int i = 0; i < nums.size(); i += 2)
            for (int j = 0; j < nums[i]; ++j)
                res.push_back(nums[i + 1]);
        return res;
    }
};
