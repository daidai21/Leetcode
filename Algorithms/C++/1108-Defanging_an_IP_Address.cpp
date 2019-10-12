// Runtime: 4 ms, faster than 54.10% of C++ online submissions for Defanging an IP Address.
// Memory Usage: 8.1 MB, less than 100.00% of C++ online submissions for Defanging an IP Address.
class Solution {
public:
    string defangIPaddr(string address) {
        string res;
        for (int i = 0; i < address.size(); ++i) {
            if (address[i] != '.')
                res += address[i];
            else
                res += "[.]";
        }
        return res;
    }
};
