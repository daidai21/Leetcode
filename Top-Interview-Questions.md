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
