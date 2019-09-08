class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        (*(digits.end() - 1))++;
        for (int i = digits.size() - 1; i >= 0; --i) {
            if (digits[i] > 9) {
                digits[i] -= 10;
                if (i > 0) {
                    digits[i - 1]++;
                } else {
                    digits.insert(digits.begin(), 1);
                }
            }
        }
        return digits;
    }
};
