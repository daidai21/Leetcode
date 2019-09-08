// Runtime: 12 ms, faster than 75.36% of C++ online submissions for Linked List Cycle II.
// Memory Usage: 9.7 MB, less than 97.62% of C++ online submissions for Linked List Cycle II.
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
    ListNode *detectCycle(ListNode *head) {
        if (head == NULL || head->next == NULL)
            return NULL;
        ListNode* fast = head;
        ListNode* slow = head;
        ListNode* entry = head;
        while (fast->next && fast->next->next) {
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow) {
                while (slow != entry) {
                    slow = slow->next;
                    entry = entry->next;
                }
                return slow;
            }
        }
        return NULL;
    }
};
