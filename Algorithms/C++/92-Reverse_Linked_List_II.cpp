// Runtime: 4 ms, faster than 72.39% of C++ online submissions for Reverse Linked List II.
// Memory Usage: 8.6 MB, less than 61.15% of C++ online submissions for Reverse Linked List II.
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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (!head)
            return NULL;
        ListNode* cur = head;
        ListNode* pre(NULL);
        while (m > 1) {
            pre = cur;
            cur = cur->next;
            --m;
            --n;
        }
        ListNode* tail = cur;
        ListNode* con = pre;
        while (n) {
            ListNode* tmp = cur->next;
            cur->next = pre;
            pre = cur;
            cur = tmp;
            --n;
        }
        if (con)
            con->next = pre;
        else
            head = pre;
        tail->next = cur;
        return head;
    }
};