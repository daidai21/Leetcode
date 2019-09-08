// Runtime: 8 ms, faster than 85.27% of C++ online submissions for Reverse Linked List.
// Memory Usage: 9.1 MB, less than 73.82% of C++ online submissions for Reverse Linked List.
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
    ListNode* reverseList(ListNode* head) {
        ListNode *cur = NULL;
        while (head) {
            ListNode *next = head -> next;
            head -> next = cur;
            cur = head;
            head = next;
        }
        return cur;
    }
};
