// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Remove Nth Node From End of List.
// Memory Usage: 8.4 MB, less than 89.92% of C++ online submissions for Remove Nth Node From End of List.
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode res(NULL);
        res.next = head;
        ListNode* p1 = &res;
        ListNode* p2 = &res;
        for (int i = 0; i < n; ++i)
            p2 = p2->next;
        while (p2->next) {
            p1 = p1->next;
            p2 = p2->next;
        }
        p1->next = p1->next->next;
        return res.next;
    }
};