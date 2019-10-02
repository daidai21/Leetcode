// Runtime: 136 ms, faster than 28.05% of C++ online submissions for Merge k Sorted Lists.
// Memory Usage: 11.3 MB, less than 50.00% of C++ online submissions for Merge k Sorted Lists.
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty())
            return nullptr;
        while (lists.size() > 1) {
            lists.push_back(merge_2_list(lists[0], lists[1]));
            lists.erase(lists.begin(), lists.begin() + 2);
        }
        return lists[0];
    }
private:
    ListNode* merge_2_list(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr)
            return l2;
        if (l2 == nullptr)
            return l1;
        if (l1->val <= l2->val) {
            l1->next = merge_2_list(l1->next, l2);
            return l1;
        }
        else {
            l2->next = merge_2_list(l1, l2->next);
            return l2;
        }
    }
};
