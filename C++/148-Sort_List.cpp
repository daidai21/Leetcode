// Runtime: 48 ms, faster than 57.26% of C++ online submissions for Sort List.
// Memory Usage: 13.6 MB, less than 15.00% of C++ online submissions for Sort List.
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
    ListNode* sortList(ListNode* head) {
        vector<int> temp;
        while (head) {
            temp.push_back(head->val);
            head = head->next;
        }
        sort(temp.begin(), temp.end());
        ListNode* res = new ListNode(NULL);
        ListNode* p = res;
        for (int val : temp) {
            p->next = new ListNode(val);
            p = p->next;
        }
        return res->next;
    }
};
