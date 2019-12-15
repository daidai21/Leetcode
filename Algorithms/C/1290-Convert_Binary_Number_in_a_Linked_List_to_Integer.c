// Runtime: 0 ms, faster than 100.00% of C online submissions for Convert Binary Number in a Linked List to Integer.
// Memory Usage: 6.9 MB, less than 100.00% of C online submissions for Convert Binary Number in a Linked List to Integer.
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


int getDecimalValue(struct ListNode* head){
    int result = 0;
    while (head != NULL) {
        result = result * 2 + head->val;
        head = head->next;
    }
    return result;
}
