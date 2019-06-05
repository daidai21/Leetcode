// Runtime: 44 ms, faster than 97.09% of C++ online submissions for Reverse String.
// Memory Usage: 15.1 MB, less than 82.16% of C++ online submissions for Reverse String.
class Solution {
public:
  void reverseString(vector<char>& s) {
    int start = 0, end = s.size() - 1;
    while (start < end) {
      swap(s[start++], s[end--]);
    }
  }
};
