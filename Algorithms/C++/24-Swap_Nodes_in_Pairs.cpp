// Runtime: 4 ms, faster than 68.83% of C++ online submissions for Swap Nodes in Pairs.
// Memory Usage: 8.7 MB, less than 44.64% of C++ online submissions for Swap Nodes in Pairs.
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
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL)
            return NULL;
        if (head->next == NULL)
            return head;
        ListNode* next = head->next;
        head->next = swapPairs(next->next);
        next->next = head;
        return next;
    }
};
