// Runtime: 20 ms, faster than 91.68% of C++ online submissions for Add Two Numbers.
// Memory Usage: 10.2 MB, less than 76.87% of C++ online submissions for Add Two Numbers.
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode res(NULL), *p = &res;
        int flag = 0;
        while (l1 || l2 || flag) {
            int add = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + flag;
            flag = add >= 10;
            p->next = new ListNode(add % 10);
            p = p->next;
            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
        }
        return res.next;
    }
};