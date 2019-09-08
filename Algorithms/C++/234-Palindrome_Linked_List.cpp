// Runtime: 24 ms, faster than 66.39% of C++ online submissions for Palindrome Linked List.
// Memory Usage: 14.4 MB, less than 6.90% of C++ online submissions for Palindrome Linked List.
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
    bool isPalindrome(ListNode* head) {
        return check(head, head);
    }
private:
    bool check(ListNode*& head, ListNode* p) {
        if (!p)
            return true;
        bool is_pal = check(head, p->next);
        if (head->val != p->val)
            return false;
        head = head->next;
        return is_pal;
    }
};
