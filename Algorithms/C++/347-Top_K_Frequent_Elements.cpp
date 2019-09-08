// Runtime: 48 ms, faster than 5.35% of C++ online submissions for Top K Frequent Elements.
// Memory Usage: 11.2 MB, less than 96.77% of C++ online submissions for Top K Frequent Elements.
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> dic;
        for (int num : nums)
            if (dic.find(num) == dic.end())
                dic[num] = 1;
            else
                ++dic[num];
        vector<int> res;
        for (int i = 0; i < k; ++i) {
            int val, freq = 0;
            for (map<int, int>::iterator it = dic.begin(); it != dic.end(); ++it)
                if (it->second > freq) {
                    freq = it->second;
                    val = it->first;
                }
            res.push_back(val);
            dic[val] = NULL;
        }
        return res;
    }
};
