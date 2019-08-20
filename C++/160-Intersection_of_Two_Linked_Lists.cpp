// Runtime: 48 ms, faster than 81.21% of C++ online submissions for Intersection of Two Linked Lists.
// Memory Usage: 16.8 MB, less than 81.48% of C++ online submissions for Intersection of Two Linked Lists.
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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (!headA || !headB)
            return NULL;
        ListNode* pa = headA, * pb = headB;
        while (pa != pb) {
            pa = pa ? pa->next : headB;
            pb = pb ? pb->next : headA;
        }
        return pa;
    }
};
