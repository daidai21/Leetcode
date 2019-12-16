#include <iostream>
#include <algorithm>
#include <vector>
#include <cassert>

using namespace std;


// binary search
class Solution {
public:
    int missingElement(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int pre = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            if (k < nums[i] - pre)
                return pre + k;
            else
                k -= nums[i] - pre - 1;
            pre = nums[i];
        }
        return pre + k;
    }
};


int main() {
    vector<int> test_case1 = {4,7,9,10};
    vector<int> test_case2 = {4,7,9,10};
    vector<int> test_case3 = {1,2,4};

    Solution s;

    assert(s.missingElement(test_case1, 1) == 5);
    assert(s.missingElement(test_case2, 3) == 8);
    assert(s.missingElement(test_case3, 3) == 6);

    cout << "OK" << endl;

    return 0;
}
