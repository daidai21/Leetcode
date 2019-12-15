// Runtime: 4 ms, faster than 40.00% of C++ online submissions for Convert Binary Number in a Linked List to Integer.
// Memory Usage: 8.4 MB, less than 100.00% of C++ online submissions for Convert Binary Number in a Linked List to Integer.
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
    int getDecimalValue(ListNode* head) {
        int result = 0;
        while (head != nullptr) {
            result = result * 2 + head->val;
            head = head->next;
        }
        return result;
    }
};
