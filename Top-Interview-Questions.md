# 1. 两数之和

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> mp;
        for (int i = 0, j; i < nums.size(); ++i) {
            j = target - nums[i];
            if (mp.find(j) != mp.end()) {
                return { mp[j], i };
            } else {
                mp[nums[i]] = i;
            }
        }
        return {};
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 
* 标签： `数组`, `哈希表`
* 难度： 简单

# 2. 两数相加

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* res = new ListNode();
        ListNode* ptr = res;
        int isCarry = 0, sm = 0;
        // l1 and l2 step
        while (l1 != NULL && l2 != NULL) {
            sm = l1->val + l2->val + isCarry;
            isCarry = sm >= 10;
            ptr->next = new ListNode(sm % 10);
            ptr = ptr->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        // l1 or l2 step
        l1 = l1 != NULL ? l1 : l2;
        while (l1 != NULL) {
            sm = l1->val + isCarry;
            isCarry = sm >= 10;
            ptr->next = new ListNode(sm % 10);
            ptr = ptr->next;
            l1 = l1->next;
        }
        // last isCarry = 1
        if (isCarry) {
            ptr->next = new ListNode(1);
        }
        return res->next;
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 
* 标签： `递归`, `链表`, `数学`
* 难度： 中等

# 3. 无重复字符的最长子串

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        std::unordered_map<char, int> mp;
        int start = 0;
        for (int end = 0; end < s.size(); ++end) {
            if (mp.find(s[end]) == mp.end()) {
                mp[s[end]] = end;
            } else {
                int tmp = mp[s[end]];
                for (int i = start; i <= tmp; ++i) {
                    mp.erase(s[i]);
                }
                start = tmp + 1;
                mp[s[end]] = end;
            }
            res = std::max(res, end - start + 1);
        }
        return res;
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(min(m, n))
* 解法： 
* 标签： `哈希表`, `字符串`, `滑动窗口`
* 难度： 中等

# 4. 寻找两个正序数组的中位数

给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

```cpp
// https://zhuanlan.zhihu.com/p/70654378
/**
 * 
 * 如图： 假设结果i， j分别在nums1， nums2中间
 * l1     i         r1  l2     j     r2
 * |----nums1--------|  |--------nums2----|
 * 
 * i->r1 + l2->j == (nums1 + nums2) / 2 == l1->i + j->r2
 * i在l1和r1之间二分搜索， 可以计算得到 l2->j = (nums1 + nums2) / 2 - l1->i
 */
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) std::swap(nums1, nums2);
        if (nums2.size() == 0) return -1; // ValueError
        int iMin = 0, iMax = nums1.size(), halfLen = (nums1.size() + nums2.size() + 1) / 2;
        while (iMin <= iMax) {
            int i = iMin + (iMax - iMin) / 2;
            int j = halfLen - i;
            if (i < nums1.size() && nums1[i] < nums2[j - 1]) {
                iMin = i + 1;
            } else if (i > 0 && nums1[i - 1] > nums2[j]) {
                iMax = i - 1;
            } else {
                int maxLeft;
                if (i == 0) {
                    maxLeft = nums2[j - 1];
                } else if (j == 0) {
                    maxLeft = nums1[i - 1];
                } else {
                    maxLeft = std::max(nums1[i - 1], nums2[j - 1]);
                }
                if ((nums1.size() + nums2.size()) % 2 == 1) { // 中位数是一个
                    return maxLeft;
                }
                int maxRight;
                if (i == nums1.size()) {
                    maxRight = nums2[j];
                } else if (j == nums2.size()) {
                    maxRight = nums1[i];
                } else {
                    maxRight = std::min(nums1[i], nums2[j]);
                }
                return (maxLeft + maxRight) / 2.0;
            }
        }
        return -1; // NonUse, for static check
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(log(min(nums1.size(),nums2.size()))
* 解法： 二分查找
* 标签： `数组`, `二分查找`, `分治`
* 难度： 困难

# 5. 最长回文子串

给你一个字符串 s，找到 s 中最长的回文子串。

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() < 2) return s;
        for (int i = 0; i < s.size(); ++i) {
            expandAroundCenter(s, i, i);
            expandAroundCenter(s, i, i + 1);
        }
        return s.substr(start, end - start + 1);
    }

private:
    int start = 0;
    int end = 0;

    void expandAroundCenter(const std::string& s, int l, int r) {
        while (l >= 0 && r < s.size() && s[l] == s[r]) {
            l--;
            r++;
        }
        if (r - l - 2 > end - start) {
            start = l + 1;
            end = r - 1;
        }
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n^2)
* 解法： 中心扩展算法
* 标签： `字符串`, `动态规划`
* 难度： 中等

# 7. 整数反转

给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。

```cpp
class Solution {
public:
    int reverse(int x) {
        long long int res = 0;
        while (x != 0) {
            res = res * 10 + x % 10;
            x = x / 10;
        }
        return (res < INT_MIN || res > INT_MAX) ? 0 : res;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 
* 标签： `数学`
* 难度： 简单

# 8. 字符串转换整数 (atoi)

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等

# 11. 盛最多水的容器

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxSpace = 0, l = 0, r = height.size() - 1;
        while (l < r) {
            maxSpace = std::max(maxSpace, std::min(height[l], height[r]) * (r - l));
            height[l] > height[r] ? r-- : l++;
        }
        return maxSpace;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 双指针+贪心
* 标签： `贪心`, `数组`, `双指针`
* 难度： 中等

# 13. 罗马数字转整数

罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
```txt
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

```cpp
class Solution {
public:
    int romanToInt(string s) {
        std::map<char, int> mp = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        int res = mp[s[s.size() - 1]];
        for (int i = s.size() - 2; i >= 0; --i) {
            res += mp[s[i]] < mp[s[i + 1]] ? -mp[s[i]] : mp[s[i]];
        }
        return res;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 
* 标签： `哈希表`, `数学`, `字符串`
* 难度： 简单

# 14. 最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) return "";
        if (strs.size() == 1) return strs[0];
        int iterLen = std::numeric_limits<int>::max();
        for (const std::string s : strs) iterLen = std::min(iterLen, (int)s.size());
        std::string res;
        for (int i = 0; i < iterLen; ++i) {
            int j = 1;
            while (j < strs.size() && strs[j - 1][i] == strs[j][i]) j++;
            if (j == strs.size()) {
                res += strs[0][i];
            } else {
                break;
            }
        }
        return res;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n^2)
* 解法： 双循环，字典树
* 标签： `字符串`
* 难度： 简单

FIXME: 字典树解法  https://leetcode.com/problems/longest-common-prefix/solution/

# 15. 三数之和

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]

提示：

0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

```cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::vector<std::vector<int>> res;
        std::sort(nums.begin(), nums.end());
        for (int i = 0; i < (int) nums.size() - 2; ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // result remove repeat
            int j = i + 1, k = nums.size() - 1;
            while (j < k) {
                int sm = nums[i] + nums[j] + nums[k];
                if (sm == 0) {
                    res.push_back(std::vector<int>{ nums[i], nums[j], nums[k] });
                    while (j + 1 < k && nums[j] == nums[j + 1]) j++;
                    while (j < k - 1 && nums[k] == nums[k - 1]) k--;
                    j++;
                    k--;
                } else if (sm > 0) {
                    k--;
                } else { // sm < 0
                    j++;
                }
            }
        }
        return res;
    }
};
```

* 空间复杂度： 
* 时间复杂度： O(n ^ 2)
* 解法： 双指针
* 标签： `数组`, `双指针`, `排序`
* 难度： 中等

# 17. 电话号码的字母组合

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等



# 19. 删除链表的倒数第 N 个结点

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

提示：

1 <= s.length <= 10^4
s 仅由括号 '()[]{}' 组成

```cpp
class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stk;
        for (const char& ch : s) {
            if (ch == '(') {
                stk.push(')');
            } else if (ch == '{') {
                stk.push('}');
            } else if (ch == '[') {
                stk.push(']');
            } else if (stk.empty() || stk.top() != ch) {
                return false;
            } else {
                stk.pop();
            }
        }
        return stk.empty();
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 
* 标签： `栈`, `字符串`
* 难度： 简单

# 21. 合并两个有序链表

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
 

提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* root = new ListNode();
        ListNode* cur = root;
        while (l1 != nullptr && l2 != nullptr) {
            if (l1->val < l2->val) {
                cur->next = l1;
                l1 = l1->next;
            } else { // l1->val >= l2->val
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        cur->next = l1 != nullptr ? l1 : l2;
        return root->next;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 
* 标签： `递归`, `链表`
* 难度： 简单


# 22. 括号生成

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]

提示：

1 <= n <= 8

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        std::vector<std::string> res;
        std::string cur = "";
        backtracking(res, n, n, cur);
        return res;
    }

private:
    void backtracking(std::vector<std::string>& res, int left, int right, std::string& cur) {
        if (left == 0 && right == 0) {
            res.push_back(cur);
            return ;
        }
        // add left
        cur += '(';
        if (left > 0) backtracking(res, left - 1, right, cur);
        cur.pop_back();
        // add right
        cur += ')';
        if (left < right && right > 0) backtracking(res, left, right - 1, cur);
        cur.pop_back();
    }
};
```

* 空间复杂度： 大约O(n)
* 时间复杂度： O((4^n) / √n)
* 解法： 回溯
* 标签： `字符串`, `动态规划`, `回溯`
* 难度： 中等

# 26. 删除有序数组中的重复项

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

提示：

0 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums 已按升序排列

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int i = 0;
        for (int j = 1; j < nums.size(); ++j) {
            if (nums[j] != nums[j - 1]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 双指针
* 标签： `数组`, `双指针`
* 难度： 简单

# 28. 实现 strStr()

实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        for (int i = 0; ; ++i) {
            for (int j = 0; ; ++j) {
                if (j == needle.size()) return i;
                if (i + j == haystack.size()) return -1;
                if (haystack[i + j] != needle[j]) break;
            }
        }
    }
};
```

FIXME: KMP 解法

* 空间复杂度： O(1)
* 时间复杂度： 
* 解法： 双指针
* 标签： `双指针`, `字符串`, `字符匹配`
* 难度： 简单


# 29. 两数相除

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等



# 34. 在排序数组中查找元素的第一个和最后一个位置

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等



# 33. 搜索旋转排序数组

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 36. 有效的数独

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 38. 外观数列

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 46. 全排列

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

```cpp
// 基于原有的，有两个元素换位置都会产生新的排列
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        std::vector<std::vector<int>> res;
        permute(nums, res, 0);
        return res;
    }

private:
    void permute(std::vector<int>& nums, 
            std::vector<std::vector<int>>& res, 
            int begin) {
        if (begin == nums.size()) {
            res.push_back(nums);
            return ;
        }
        for (int i = begin; i < nums.size(); ++i) {
            std::swap(nums[begin], nums[i]);
            permute(nums, res, begin + 1);
            std::swap(nums[begin], nums[i]);
        }
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(n^2)
* 解法： 
* 标签： `数组`, `回溯`
* 难度： 中等

# 48. 旋转图像

给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        transpose(matrix);
        reverse(matrix);
        return;
    }

private:
    void reverse(std::vector<std::vector<int>>& matrix) { // 左右对称
        for (int i = 0; i < matrix.size(); ++i) {
            for (int j = 0; j < matrix[0].size() / 2; ++j) {
                std::swap(matrix[i][j], matrix[i][matrix[0].size() - j - 1]);
            }
        }
    }

    void transpose(std::vector<std::vector<int>>& matrix) { // 左上角到右下角为对称线条
        for (int i = 0; i < matrix.size(); ++i) {
            for (int j = i; j < matrix[0].size(); ++j) {
                std::swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n^2)
* 解法： 
* 标签： `数组`, `数学`, `矩阵`
* 难度： 中等

# 49. 字母异位词分组

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 50. Pow(x, n)

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 53. 最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        std::vector<int> dp(nums.size(), nums[0]);
        int mx = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            dp[i] = nums[i] + std::max(dp[i - 1], 0);
            mx = std::max(mx, dp[i]);
        }
        return mx;
    }
};

// 上边的dp空间优化到O(1)
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int i = nums[0], j = nums[0];
        for (int k = 1; k < nums.size(); ++k) {
            i = std::max(nums[k] + i, nums[k]);
            j = std::max(j, i);
        }
        return j;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： dp
* 标签： `数组`, `分治`, `动态规划`
* 难度： 简单

# 54. 螺旋矩阵

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 55. 跳跃游戏

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 56. 合并区间

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 62. 不同路径

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等

# 66. 加一

给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        bool isCarry = true;
        for (int i = digits.size() - 1; i >= 0; --i) {
            digits[i] += isCarry;
            isCarry = digits[i] > 9;
            digits[i] %= 10;
        }
        if (isCarry) {
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 
* 标签： `数组`, `数学`
* 难度： 简单

# 69. x 的平方根

实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。

```cpp
class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) return 0;
        int l = 1, r = x / 2, mid;
        while (l < r) {
            mid = l + (r - l) / 2;
            if (mid <= x / mid && (mid + 1) > x / (mid + 1)) {
                return mid;
            } else if (mid > x / mid) {
                r = mid - 1;
            } else if (mid < x / mid) {
                l = mid + 1;
            }
        }
        return l;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(log n)
* 解法： 二分查找
* 标签： `数学`, `二分查找`
* 难度： 简单

# 70. 爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

```cpp
// dp
// 空间O(n), 时间O(n)
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        std::vector<int> arr(n);
        arr[0] = 1; // 爬一个台阶有一种方法
        arr[1] = 2; // 爬两个台阶有两种方法
        for (int i = 2; i < n; ++i) arr[i] = arr[i - 1] + arr[i - 2];
        return arr[n - 1];
    }
};

// dp空间优化
// 空间O(1), 时间O(n)
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        int pre = 1, cur = 2, tmp = 0;
        for (int i = 2; i < n; ++i) {
            tmp = pre + cur;
            pre = cur;
            cur = tmp;
        }
        return cur;
    }
};

// 递归+mem
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        std::vector<int> mem(n + 1, -1);
        mem[1] = 1;
        mem[2] = 2;
        return recursion(n, mem);
    }

private:
    int recursion(int n, std::vector<int>& mem) {
        if (mem[n] != -1) return mem[n];
        mem[n] = recursion(n - 1, mem) + recursion(n - 2, mem);
        return mem[n];
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)； 最优是O(log n)，用的数学fib函数
* 解法： dp， 递归+mem
* 标签： `记忆化搜索`, `数学`, `动态规划`
* 难度： 简单

# 73. 矩阵置零

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 75. 颜色分类

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等

# 78. 子集

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

```cpp
// 回溯
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        std::vector<std::vector<int>> res;
        std::vector<int> cur;
        backtracking(nums, res, 0, cur);
        return res;
    }

private:
    void backtracking(std::vector<int>& nums, 
            std::vector<std::vector<int>>& res, 
            int idx, 
            std::vector<int>& cur) {
        if (idx >= nums.size()) {
            res.push_back(cur);
            return;
        }
        backtracking(nums, res, idx + 1, cur);
        cur.push_back(nums[idx]);
        backtracking(nums, res, idx + 1, cur);
        cur.pop_back();
    }
};

// 位运算
// 集合长度为n，子集数量为2^n个
// [], [ ], [ ], [    ], [ ], [    ], [    ], [       ]
// [], [1], [ ], [1   ], [ ], [1   ], [    ], [1      ]
// [], [1], [2], [1, 2], [ ], [1   ], [2   ], [1, 2   ]
// [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]
// 以[1, 2, 3]为例，1在每两个连续子集中出现一次，2在每四个连续子集中出现两次，3在每八个子集中出现四次（最初所有子集都是空的）
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int p = 1 << nums.size(); // 初始化子集数量
        std::vector<std::vector<int>> res(p);
        for (int i = 0; i < p; ++i) { // 每个子集迭代
            for (int j = 0; j < nums.size(); ++j) { // 每个元素迭代
                if ((i >> j) & 1) {
                    res[i].push_back(nums[j]);
                }
            }
        }
        return res;
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(n^2)
* 解法： 回溯，位运算
* 标签： `位运算`, `数组`, `回溯`
* 难度： 中等

# 79. 单词搜索

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等

# 91. 解码方法

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等



# 94. 二叉树的中序遍历

给定一个二叉树的根节点 root ，返回它的 中序 遍历。

```cpp
// 递归
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        std::vector<int> res;
        recursion(root, res);
        return res;
    }

private:
    void recursion(TreeNode* node, std::vector<int>& vec) {
        if (node == NULL) return;
        if (node->left != NULL) recursion(node->left, vec);
        vec.push_back(node->val);
        if (node->right != NULL) recursion(node->right, vec);
    }
};

// 迭代
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        std::stack<TreeNode*> stk;
        std::vector<int> res;
        TreeNode* cur = root;
        while (cur != NULL || !stk.empty()) {
            while (cur != NULL) {
                stk.push(cur);
                cur = cur->left;
            }
            cur = stk.top();
            stk.pop();
            res.push_back(cur->val);
            cur = cur->right;
        }
        return res;
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 递归，迭代
* 标签： `栈`, `树`, `深度优先搜索`, `二叉树`
* 难度： 简单

# 98. 验证二叉搜索树

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

```cpp
// 递归
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return isValidBST(root, std::numeric_limits<long int>::min(), std::numeric_limits<long int>::max());
    }

private:
    bool isValidBST(TreeNode* root, long int minVal, long int maxVal) {
        if (root == nullptr) return true;
        if (root->val >= maxVal || root->val <= minVal) return false;
        return isValidBST(root->left, minVal, root->val) && isValidBST(root->right, root->val, maxVal);
    }
};

// 迭代
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if (root == nullptr) return true;
        std::stack<TreeNode*> stk;
        TreeNode* pre = nullptr;
        while (root != nullptr || !stk.empty()) {
            while (root != nullptr) {
                stk.push(root);
                root = root->left;
            }
            root = stk.top();
            stk.pop();
            if (pre != nullptr && pre->val >= root->val) return false;
            pre = root;
            root = root->right;
        }
        return true;
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 递归，迭代
* 标签： `树`, `深度优先搜索`, `二叉搜索树`, `二叉树`
* 难度： 中等

# 101. 对称二叉树

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

```txt
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

```txt
    1
   / \
  2   2
   \   \
   3    3
```

进阶： 你可以运用递归和迭代两种方法解决这个问题吗？

```cpp
// 递归
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        return recursion(root->left, root->right);
    }

private:
    bool recursion(TreeNode* left, TreeNode* right) {
        if (left == NULL && right == NULL) return true;
        if (left == NULL || right == NULL) return false;
        return (left->val == right->val) && recursion(left->left, right->right) && recursion(left->right, right->left);
    }
};

// 迭代
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        std::stack<TreeNode*> stk;
        stk.push(root);
        stk.push(root);
        TreeNode* node1;
        TreeNode* node2;
        while (!stk.empty()) {
            node1 = stk.top();
            stk.pop();
            node2 = stk.top();
            stk.pop();
            if (node1 == NULL && node2 == NULL) continue;
            if (node1 == NULL || node2 == NULL) return false;
            if (node1->val != node2->val) return false;
            stk.push(node1->left);
            stk.push(node2->right);
            stk.push(node1->right);
            stk.push(node2->left);
        }
        return true;
    }
};
```

* 空间复杂度： 
* 时间复杂度： O(n)
* 解法： 
* 标签： `树`, `深度优先搜索`, `广度优先搜索`, `二叉树`
* 难度： 简单

# 102. 二叉树的层序遍历

给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

```cpp
// 迭代，按层遍历
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        std::vector<std::vector<int>> res;
        if (root == NULL) return res;
        std::vector<TreeNode*> lyr = { root };
        while (!lyr.empty()) {
            std::vector<int> lyrVal;
            std::vector<TreeNode*> lyrNxt;
            for (TreeNode* node : lyr) {
                lyrVal.push_back(node->val);
                if (node->left != NULL) lyrNxt.push_back(node->left);
                if (node->right != NULL) lyrNxt.push_back(node->right);
            }
            lyr = lyrNxt;
            res.push_back(lyrVal);
        }
        return res;
    }
};

// 递归
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        std::vector<std::vector<int>> res;
        buldLyr(root, 0, res);
        return res;
    }

private:
    void buldLyr(TreeNode* node, int depth, std::vector<std::vector<int>>& vec) {
        if (node == NULL) return;
        if (vec.size() == depth) vec.push_back(std::vector<int>());
        vec[depth].push_back(node->val);
        buldLyr(node->left, depth + 1, vec);
        buldLyr(node->right, depth + 1, vec);
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 递归，迭代
* 标签： `树`, `广度优先搜索`, `二叉树`
* 难度： 中等

# 103. 二叉树的锯齿形层序遍历

给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],
```txt
    3
   / \
  9  20
    /  \
   15   7
```
返回锯齿形层序遍历如下：
```txt
[
  [3],
  [20,9],
  [15,7]
]
```

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        std::vector<std::vector<int>> res;
        if (root == nullptr) return res;
        std::vector<TreeNode*> layer = { root };
        while (!layer.empty()) {
            std::vector<TreeNode*> nextLayer;
            std::vector<int> layerValues;
            for (TreeNode* node : layer) {
                layerValues.push_back(node->val);
                if (node->left  != nullptr) nextLayer.push_back(node->left);
                if (node->right != nullptr) nextLayer.push_back(node->right);
            }
            layer = nextLayer;
            res.push_back(layerValues);
        }
        for (int i = 1; i < res.size(); i += 2) {
            for (int j = 0; j < res[i].size() / 2; ++j) {
                std::swap(res[i][j], res[i][res[i].size() - j - 1]);
            }
        }
        return res;
    }
};
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 广度优先搜索-迭代
* 标签： `树`, `广度优先搜索`, `二叉树`
* 难度： 中等

# 104. 二叉树的最大深度

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

```txt
    3
   / \
  9  20
    /  \
   15   7
```

返回它的最大深度 3 。

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL) return 0;
        return std::max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： 
* 解法： 递归
* 标签： `树`, `深度优先搜索`, `广度优先搜索`, `二叉树`
* 难度： 简单




# 105. 从前序与中序遍历序列构造二叉树

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 108. 将有序数组转换为二叉搜索树

给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案

输入：nums = [1,3]
输出：[3,1]
解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。

提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 按 严格递增 顺序排列

```cpp
// 递归+分治
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (nums.size() == 0) return NULL;
        return helper(nums, 0, nums.size() - 1);
    }

private:
    TreeNode* helper(const std::vector<int>& nums, int left, int right) {
        if (left > right) return NULL;
        int mid = left + (right - left) / 2;
        TreeNode* node = new TreeNode(nums[mid]);
        node->left = helper(nums, left, mid - 1);
        node->right = helper(nums, mid + 1, right);
        return node;
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 递归+分治
* 标签： `树`, `二叉搜索树`, `数组`, `分治`, `二叉树`
* 难度： 简单

# 116. 填充每个节点的下一个右侧节点指针

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等

# 118. 杨辉三角

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
```txt
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

```cpp
// 模拟
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        std::vector<std::vector<int>> res;
        for (int i = 1; i <= numRows; ++i) {
            std::vector<int> lyr;
            if (i == 1) {
                lyr.push_back(1);
            } else if (i == 2) {
                lyr.push_back(1);
                lyr.push_back(1);
            } else {
                lyr.push_back(1);
                for (int j = 1; j <= i - 2; ++j) lyr.push_back(res[i - 2][j - 1] + res[i - 2][j]);
                lyr.push_back(1);
            }
            res.push_back(lyr);
        }
        return res;
    }
};
```

* 空间复杂度： O(n^2)
* 时间复杂度： O(n^2)
* 解法： dp，模拟
* 标签： `数组`, `动态规划`
* 难度： 简单

# 121. 买卖股票的最佳时机

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

提示：

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = std::numeric_limits<int>::max(), res = 0;
        for (const int& price : prices) {
            if (price < minPrice) {
                minPrice = price;
            } else if (price - minPrice > res) {
                res = price - minPrice;
            }
        }
        return res;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： dp
* 标签： `数组`, `动态规划`
* 难度： 简单

# 122. 买卖股票的最佳时机 II

给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:

输入: prices = [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: prices = [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

提示：

1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4

```cpp
// 只计算股票增加的价格
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        for (int i = 1; i < prices.size(); ++i) {
            if (prices[i] > prices[i - 1]) res += prices[i] - prices[i - 1];
        }
        return res;
    }
};

// 计算峰顶和峰谷的差值
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i = 0, peak = prices[0], valley = prices[0], res = 0;
        while (i < prices.size() - 1) {
            // find peak
            while (i < prices.size() - 1 && prices[i] >= prices[i + 1]) i++;
            peak = prices[i];
            // find valley
            while (i < prices.size() - 1 && prices[i] <= prices[i + 1]) i++;
            valley = prices[i];
            res += valley - peak;
        }
        return res;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： dp
* 标签： `贪心`, `数组`, `动态规划`
* 难度： 简单

# 125. 验证回文串

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        if (s.empty()) return true;
        int l = 0, r = s.size() - 1;
        while (l <= r) {
            if (!std::isalnum(s[l])) {
                l++;
            } else if (!std::isalnum(s[r])) {
                r--;
            } else {
                if (std::tolower(s[l]) != std::tolower(s[r])) return false;
                l++;
                r--;
            }
        }
        return true;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 双指针
* 标签： `双指针`, `字符串`
* 难度： 简单

# 128. 最长连续序列

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等
# 130. 被围绕的区域

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 131. 分割回文串

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等

# 134. 加油站

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 136. 只出现一次的数字

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (int num : nums) res ^= num;
        return res;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： a xor a = 0
* 标签： `位运算`, `数组`
* 难度： 简单


# 138. 复制带随机指针的链表

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 139. 单词拆分

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等

# 141. 环形链表

给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。

进阶：你能用 O(1)（即，常量）内存解决此问题吗？

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == NULL) return false;
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != NULL && fast->next->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) return true;
        }
        return false;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 双指针
* 标签： `哈希表`, `链表`, `双指针`
* 难度： 简单


# 146. LRU 缓存机制

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 148. 排序链表

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 150. 逆波兰表达式求值

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 152. 乘积最大子数组

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等

# 155. 最小栈

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

提示：

pop、top 和 getMin 操作总是在 非空栈 上调用。

```cpp
class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {}
    
    void push(int val) {
        stk.push(val);
        minStk.empty() ? minStk.push(val) : minStk.push(std::min(val, minStk.top()));
    }
    
    void pop() {
        stk.pop();
        minStk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return minStk.top();
    }

private:
    std::stack<int> minStk;
    std::stack<int> stk;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```

* 空间复杂度： O(2n)
* 时间复杂度： O(1)
* 解法： 双栈
* 标签： `栈`, `设计`
* 难度： 简单

# 160. 相交链表

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

```cpp
// 哈希表
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        std::unordered_set<ListNode*> st;
        while (headA) {
            st.insert(headA);
            headA = headA->next;
        }
        while (headB) {
            if (st.find(headB) != st.end()) return headB;
            headB = headB->next;
        }
        return nullptr;
    }
};

// 双指针
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == nullptr || headB == nullptr) return nullptr;
        ListNode* p1 = headA, * p2 = headB;
        while (p1 && p2 && p1 != p2) {
            p1 = p1->next;
            p2 = p2->next;
            if (p1 == p2) return p1;
            if (p1 == nullptr) p1 = headB;
            if (p2 == nullptr) p2 = headA;
        }
        return p1;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 
* 标签： `哈希表`, `链表`, `双指针`
* 难度： 简单

# 162. 寻找峰值

峰值元素是指其值大于左右相邻值的元素。

给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

```cpp
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[mid + 1]) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(logN)
* 解法： 
* 标签： `数组`, `二分查找`
* 难度： 中等

# 163. 缺失的区间

给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。

示例：

输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
输出: ["2", "4->49", "51->74", "76->99"]

```cpp
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
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 
* 标签： `哈希表`, `链表`, `双指针`
* 难度： 简单

# 166. 分数到小数

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 171. Excel表列序号

给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

```txt
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
```

示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701

```cpp
class Solution {
public:
    int titleToNumber(string columnTitle) {
        int res = 0;
        for (int i = 0; i < columnTitle.size(); ++i) res = res * 26 + (columnTitle[i] - 'A' + 1);
        return res;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 
* 标签： `数学`, `字符串`
* 难度： 简单

# 172. 阶乘后的零

给定一个整数 n，返回 n! 结果尾数中零的数量。

```cpp
class Solution {
public:
    int trailingZeroes(int n) {
        return n == 0 ? 0 : n / 5 + trailingZeroes(n / 5);
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(log n)
* 解法： 组成0的数的因子为2 * 5， 因子2是充足的，只需要计算5的因子数量就好了
* 标签： `数学`
* 难度： 简单

# 179. 最大数

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等

# 189. 旋转数组

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 190. 颠倒二进制位

颠倒给定的 32 位无符号整数的二进制位。

提示：

请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 2 中，输入表示有符号整数 -3，输出表示有符号整数 -1073741825。

进阶: 如果多次调用这个函数，你将如何优化你的算法？

```cpp
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0, power = 31;
        while (n != 0) {
            res += (n & 1) << power;
            n >>= 1;
            power--;
        }
        return res;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 位运算
* 标签： `位运算`, `分治`
* 难度： 简单

# 191. 位1的个数

编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

提示：

请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。

提示：输入必须是长度为 32 的 二进制串 。
进阶：如果多次调用这个函数，你将如何优化你的算法？

```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int bits = 0;
        unsigned int mask = 1;
        for (int i = 0; i < 32; ++i) {
            if ((n & mask) != 0) bits++;
            mask <<= 1;
        }
        return bits;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(1)
* 解法： 位运算
* 标签： `位运算`
* 难度： 简单

# 198. 打家劫舍

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等

# 200. 岛屿数量

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等

# 202. 快乐数

编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true ；不是，则返回 false 。

示例 1：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
示例 2：

输入：n = 2
输出：false

提示： 1 <= n <= 2^31 - 1

```cpp
class Solution {
public:
    bool isHappy(int n) {
        int slow = n, fast = n;
        do {
            slow = digitSquareSum(slow);
            fast = digitSquareSum(fast);
            fast = digitSquareSum(fast);
        } while (slow != fast);
        return slow == 1;
    }

private:
    int digitSquareSum(int n) {
        int sm = 0, tmp;
        while (n) {
            tmp = n % 10;
            sm += tmp * tmp;
            n /= 10;
        }
        return sm;
    }
};
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： `哈希表`, `数字`, `双指针`
* 难度： 简单

# 204. 计数质数

统计所有小于非负整数 n 的质数的数量。

```cpp
class Solution {
public:
    int countPrimes(int n) {
        std::vector<int> isPrimes(n, true);
        int cnt = 0;
        for (int i = 2; i < n; ++i) {
            if (isPrimes[i]) {
                cnt++;
                for (long int j = i; i * j < n; ++j) {
                    isPrimes[i * j] = false;
                }
            }
        }
        return cnt;
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 
* 标签： `数组`, `数字`, `枚举`, `数论`
* 难度： 简单

# 206. 反转链表

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* cur = head;
        ListNode* pre = NULL;
        while (cur != NULL) {
            ListNode* tmp = cur->next;
            cur->next = pre;
            pre = cur;
            cur = tmp;
        }
        return pre;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 
* 标签： `递归`, `链表`
* 难度： 简单


# 207. 课程表

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 208. 实现 Trie (前缀树)

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等



# 210. 课程表 II

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 215. 数组中的第K个最大元素

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等



# 217. 存在重复元素

给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

```cpp
// sort
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        for (int i = 1; i < nums.size(); ++i) if (nums[i] == nums[i - 1]) return true;
        return false;
    }
};

// hashTable
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> st;
        for (int num : nums) {
            if (st.find(num) != st.end()) return true;
            st.insert(num);
        }
        return false;
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 
* 标签： `递归`, `链表`
* 难度： 简单


# 227. 基本计算器 II

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等



# 230. 二叉搜索树中第K小的元素

给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

提示：

树中的节点数为 n 。
1 <= k <= n <= 104
0 <= Node.val <= 104
 
进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        std::stack<TreeNode*> stk;
        while (true) {
            while (root != nullptr) {
                stk.push(root);
                root = root->left;
            }
            root = stk.top();
            stk.pop();
            k--;
            if (k == 0) return root->val;
            root = root->right;
        }
        return -1;
    }
};
```

* 空间复杂度： O(h + k), h为树高
* 时间复杂度： O(k)
* 解法： 迭代+前序遍历
* 标签： `树`, `深度优先搜索`, `二叉搜索树`, `二叉树`
* 难度： 中等

# 234. 回文链表

请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        // find mid ptr
        ListNode* fastPtr = head;
        ListNode* slowPtr = head;
        while (fastPtr->next != NULL && fastPtr->next->next != NULL) {
            fastPtr = fastPtr->next->next;
            slowPtr = slowPtr->next;
        }
        if (fastPtr->next != NULL) slowPtr = slowPtr->next; // 如果节点数为奇数，中间的那个直接忽略，left链表会比right链表多一个节点，但是最后不用比较
        // reverse mid right
        ListNode* pre = NULL;
        ListNode* cur = slowPtr;
        while (cur != NULL) {
            ListNode* tmp = cur->next;
            cur->next = pre;
            pre = cur;
            cur = tmp;
        }
        // compare left and right
        while (pre != NULL) {
            if (pre->val != head->val) return false;
            pre = pre->next;
            head = head->next;
        }
        return true;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 
* 标签： `栈`, `递归`, `链表`, `双指针`
* 难度： 简单



# 236. 二叉树的最近公共祖先

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr || root == p || root == q) return root; // 如果root已经空了，返回root，也就是null；如果root知道一个，返回root
        TreeNode* left  = lowestCommonAncestor(root->left,  p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        if (left == nullptr) { // 说明都在right下找到了
            return right;
        } else if (right == nullptr) { // 说明都在left下找到了
            return left;
        } else { // 说明分别在left和right下，所以要返回root
            return root;
        }
    }
};
// FIXME:迭代写法
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 递归/迭代，深度优先搜索
* 标签： `树`, `深度优先搜索`, `二叉树`
* 难度： 中等


# 237. 删除链表中的节点

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(1)
* 解法： 
* 标签： `链表`
* 难度： 简单


# 238. 除自身以外数组的乘积

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等



# 242. 有效的字母异位词

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

```cpp
// 排序
// 时间 O(nlogn)
// 空间 O(1)
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());
        return s == t;        
    }
};

// 哈希表
// 时间 O(n)
// 空间 O(1)
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::vector<int> mpS(26, 0), mpT(26, 0);
        for (const char& ch : s) mpS[ch - 'a']++;
        for (const char& ch : t) mpT[ch - 'a']++;
        return mpS == mpT;
    }
};
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： `哈希表`, `字符串`, `排序`
* 难度： 简单


# 251. 展开二维向量

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等

# 253. 会议室 II

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 268. 丢失的数字

给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

进阶： 你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?

示例 1：

输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
示例 2：

输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
示例 3：

输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。
示例 4：

输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。

提示：

n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
nums 中的所有数字都 独一无二

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int expectSum = nums.size() * (nums.size() + 1) / 2;
        int actualSum = 0;
        for (const int& num : nums) actualSum += num;
        return expectSum - actualSum;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 数学
* 标签： `位运算`, `数组`, `哈希表`, `数学`, `排序`
* 难度： 简单


# 277. 搜寻名人

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 279. 完全平方数

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等



# 283. 移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

```cpp
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for (int i = 0, lastZeroIdx = 0; i < nums.size(); ++i) {
            if (nums[i] != 0) {
                std::swap(nums[lastZeroIdx], nums[i]);
                lastZeroIdx++;
            }
        }
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 
* 标签： `数组`, `双指针`
* 难度： 简单



# 285. 二叉搜索树中的中序后继

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 287. 寻找重复数

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 289. 生命游戏

根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。

```cpp
// State transitions
//  0 : dead to dead
//  1 : live to live
//  2 : live to dead
//  3 : dead to live
// 
// live 1, dead 0
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {

        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                int nextSurviveStatus =  canSurvive(board, i, j);
                if (board[i][j] == 1) {
                    board[i][j] = nextSurviveStatus ? 1 : 2;
                } else { // board[i][j] == 0
                    board[i][j] = nextSurviveStatus ? 3 : 0;
                }
            }
        }
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                if (board[i][j] == 2) {
                    board[i][j] = 0;
                } else if (board[i][j] == 3) {
                    board[i][j] = 1;
                }
            }
        }
        return;
    }

private:
    bool canSurvive(const std::vector<std::vector<int>>& board, int i, int j) {
        int aroundSurviveNum = 0;
        // from left up, clockwise
        if (i - 1 >= 0 && j - 1 >= 0)                           aroundSurviveNum += board[i - 1][j - 1] == 1 || board[i - 1][j - 1] == 2; // left up
        if (i - 1 >= 0)                                         aroundSurviveNum += board[i - 1][j]     == 1 || board[i - 1][j]     == 2; // up
        if (i - 1 >= 0 && j + 1 < board[0].size())              aroundSurviveNum += board[i - 1][j + 1] == 1 || board[i - 1][j + 1] == 2; // right up
        if (j + 1 < board[0].size())                            aroundSurviveNum += board[i][j + 1]     == 1 || board[i][j + 1]     == 2; // right
        if (i + 1 < board.size() && j + 1 < board[0].size())    aroundSurviveNum += board[i + 1][j + 1] == 1 || board[i + 1][j + 1] == 2; // right down
        if (i + 1 < board.size())                            aroundSurviveNum += board[i + 1][j]     == 1 || board[i + 1][j]     == 2; // down
        if (i + 1 < board.size() && j - 1 >= 0)                 aroundSurviveNum += board[i + 1][j - 1] == 1 || board[i + 1][j - 1] == 2; // left down
        if (j - 1 >= 0)                                         aroundSurviveNum += board[i][j - 1]     == 1 || board[i][j - 1]     == 2; // left
        // judge result
        bool result = board[i][j] == 1 || board[i][j] == 2;
        if (result) {
            if (aroundSurviveNum < 2) {
                result = false;
            } else if (aroundSurviveNum == 2 || aroundSurviveNum == 3) {
                result = true;
            } else if (aroundSurviveNum > 3) {
                result = false;
            }
        } else { // board[i][j] == 0 || board[i][j] == 3
            if (aroundSurviveNum == 3) {
                result = true;
            }
        }
        return result;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(m * n)
* 解法： 模拟+状态压缩
* 标签： `数组`, `矩阵`, `模拟`
* 难度： 中等


# 300. 最长递增子序列

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 322. 零钱兑换

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 324. 摆动排序 II

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等



# 326. 3的幂

给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3^x

```cpp
class Solution {
public:
    bool isPowerOfThree(int n) {
        long int pw = 1;
        while (pw < n) pw *= 3;
        return pw == n;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 
* 标签： `递归`, `数学`
* 难度： 简单


# 328. 奇偶链表

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等

# 334. 递增的三元子序列

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等



# 340. 至多包含K 个不同字符的最长子串

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 341. 扁平化嵌套列表迭代器

给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。

示例 1:

输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
示例 2:

输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。

```cpp
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        for (int i = nestedList.size() - 1; i >= 0; --i) {
            stk.push(&nestedList[i]);
        }
    }
    
    int next() {
        int nxt = stk.top()->getInteger();
        stk.pop();
        return nxt;
    }
    
    bool hasNext() {
        while (!stk.empty()) {
            NestedInteger* p = stk.top();
            if (p->isInteger()) return true;
            std::vector<NestedInteger> & vec = p->getList();
            stk.pop();
            for (int i = vec.size() - 1; i >= 0; --i) {
                stk.push(&vec[i]);
            }
        }
        return false;
    }

private:
    std::stack<NestedInteger*> stk;
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 
* 标签： `栈`, `树`, `深度优先搜索`, `设计`, `队列`, `迭代器`
* 难度： 中等

# 344. 反转字符串

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

 

示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]

```cpp
class Solution {
public:
    void reverseString(vector<char>& s) {
        int left = 0, right = s.size() - 1, tmp;
        while (left < right) {
            tmp = s[left];
            s[left] = s[right];
            s[right] = tmp;
            left++;
            right--;
        }
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： 
* 解法： 双指针
* 标签： `递归`, `双指针`, `字符串`
* 难度： 简单



# 347. 前 K 个高频元素

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 348. 设计井字棋

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 350. 两个数组的交集 II

给定两个数组，编写一个函数来计算它们的交集。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

```cpp
// 双指针
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        std::sort(nums1.begin(), nums1.end());
        std::sort(nums2.begin(), nums2.end());
        int s1 = 0, s2 = 0;
        std::vector<int> res;
        while (s1 < nums1.size() && s2 < nums2.size()) {
            if (nums1[s1] == nums2[s2]) {
                res.push_back(nums1[s1]);
                s1++;
                s2++;
            } else if (nums1[s1] < nums2[s2]) {
                s1++;
            } else { // nums1[s1] > nums2[s2]
                s2++;
            }
        }
        return res;
    }
};

// 哈希表
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) std::swap(nums1, nums2); // make num1 length min
        std::map<int, int> cntNums2;
        std::vector<int> res;
        for (int num : nums2) cntNums2.find(num) != cntNums2.end() ? cntNums2[num]++ : cntNums2[num] = 1;
        for (int num : nums1) {
            if (cntNums2.find(num) != cntNums2.end() && cntNums2[num] > 0) {
                res.push_back(num);
                cntNums2[num]--;
            }
        }
        return res;
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 双指针，哈希表
* 标签： `数组`, `哈希表`, `双指针`, `二分查找`, `排序`
* 难度： 简单

# 371. 两整数之和

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 378. 有序矩阵中第 K 小的元素

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 380. O(1) 时间插入、删除和获取随机元素

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 384. 打乱数组

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等



# 387. 字符串中的第一个唯一字符

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

提示：你可以假定该字符串只包含小写字母。

```cpp
class Solution {
public:
    int firstUniqChar(string s) {
        std::unordered_map<char, int> cnt;
        for (const char& ch : s) cnt.find(ch) != cnt.end() ? cnt[ch]++ : cnt[ch] = 1;
        for (int i = 0; i < s.size(); ++i) if (cnt[s[i]] == 1) return i;
        return -1;
    }
};

class Solution {
public:
    int firstUniqChar(string s) {
        std::vector<int> minIdx(26, s.size());
        std::vector<int> existsTimes(26, 0);
        for (int i = 0; i < s.size(); ++i) {
            existsTimes[s[i] - 'a']++;
            minIdx[s[i] - 'a'] = std::min(minIdx[s[i] - 'a'], i);
        }
        int res = s.size();
        for (int i = 0; i < 26; ++i) if (existsTimes[i] == 1) res = std::min(res, minIdx[i]);
        return res == s.size() ? -1 : res;
    }
};
```

* 空间复杂度： O(1)
* 时间复杂度： O(n)
* 解法： 
* 标签： `队列`, `哈希表`, `字符串`, `计数`
* 难度： 简单



# 395. 至少有 K 个重复字符的最长子串

TODO

```cpp
```

* 空间复杂度： 
* 时间复杂度： 
* 解法： 
* 标签： ``, ``
* 难度： 中等


# 412. Fizz Buzz

写一个程序，输出从 1 到 n 数字的字符串表示。

1.如果 n 是3的倍数，输出“Fizz”；
2.如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：n = 15,
返回:

```txt
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
```

```cpp
class Solution {
public:
    vector<string> fizzBuzz(int n) {
        std::vector<std::string> res;
        for (int i = 1; i <= n; ++i) {
            if (i % 3 == 0 && i % 5 == 0) {
                res.push_back("FizzBuzz");
            } else if (i % 3 == 0) {
                res.push_back("Fizz");
            } else if (i % 5 == 0) {
                res.push_back("Buzz");
            } else {
                res.push_back(std::to_string(i));
            }
        }
        return res;
    }
};
```

* 空间复杂度： O(n)
* 时间复杂度： O(n)
* 解法： 
* 标签： `数学`, `字符串`, `模拟`
* 难度： 简单

# 454. 四数相加 II

给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -2^28 到 2^28 - 1 之间，最终结果不会超过 2^31 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

```cpp
class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        std::unordered_map<int, int> mp;
        int res = 0;
        for (const int& n1 : nums1) {
            for (const int& n2 : nums2) {
                mp.find(n1 + n2) != mp.end() ? mp[n1 + n2]++ : mp[n1 + n2] = 1;
            }
        }
        for (const int& n3 : nums3) {
            for (const int& n4 : nums4) {
                if (mp.find(0 - n3 - n4) != mp.end()) res += mp[0 - n3 - n4];
            }
        }
        return res;
    }
};
```

* 空间复杂度： 
* 时间复杂度： O(n ^ 2)
* 解法： 哈希表
* 标签： `数组`, `哈希表`
* 难度： 中等
