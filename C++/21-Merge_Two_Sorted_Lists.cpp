// Runtime: 8 ms, faster than 82.61% of C++ online submissions for Merge Two Sorted Lists.
// Memory Usage: 9 MB, less than 28.99% of C++ online submissions for Merge Two Sorted Lists.
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        while (l1 && l2) {
            ListNode*& node = l1->val < l2->val ? l1 : l2;
            tail = tail->next = node;
            node = node->next;
        }
        tail->next = l1 ? l1 : l2;
        return dummy.next;
    }
};