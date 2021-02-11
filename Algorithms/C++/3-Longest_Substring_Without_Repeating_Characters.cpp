// Runtime: 8 ms, faster than 95.93% of C++ online submissions for Longest Substring Without Repeating Characters.
// Memory Usage: 10.4 MB, less than 67.18% of C++ online submissions for Longest Substring Without Repeating Characters.
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> dic(256, -1);
        int max_len = 0, start = -1;
        for (int i = 0; i != s.length(); ++i) {
            if (dic[s[i]] > start)
                start = dic[s[i]];
            dic[s[i]] = i;
            max_len = max(max_len, i - start);
        }
        return max_len;
    }
};


// Runtime: 8 ms, faster than 89.20% of C++ online submissions for Longest Substring Without Repeating Characters.
// Memory Usage: 7.4 MB, less than 82.40% of C++ online submissions for Longest Substring Without Repeating Characters.
/**
 * 最优解
 */
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        vector<int> mp(128, 0);
        for (int i = 0, j = 0; j < s.size(); ++j) {
            i = std::max(mp[s[j]], i);
            ans = std::max(ans, j - i + 1);
            mp[s[j]] = j + 1; // 存储的是[1, ..., s.size()]，对应[0, ..., s.size() - 1]
        }
        return ans;
    }
};



// Runtime: 28 ms, faster than 56.00% of C++ online submissions for Longest Substring Without Repeating Characters.
// Memory Usage: 10.8 MB, less than 27.99% of C++ online submissions for Longest Substring Without Repeating Characters.
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0,
            left = 0, // left pointer
            right = 0; // right pointer
        std::unordered_set<char> st; // sliding window
        while (left < s.size() && right < s.size()) {
            if (st.find(s[right]) == st.end()) { // contain
                st.insert(s[right]);
                right++;
                ans = std::max(ans, right - left);
            } else { // not contain, 删除left到重复的所有元素
                st.erase(s[left]);
                left++;
            }
            // cout << left << " " << right << endl;
        }
        return ans;
    }
};
