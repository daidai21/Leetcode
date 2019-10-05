// Runtime: 16 ms, faster than 96.80% of C++ online submissions for Reverse Nodes in k-Group.
// Memory Usage: 10.8 MB, less than 6.45% of C++ online submissions for Reverse Nodes in k-Group.
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        vector<int> tmp;
        while (head) {
            tmp.push_back(head->val);
            head = head->next;
        }
        for (int i = 0; i + k <= tmp.size(); i += k)
            reverse(tmp.begin() + i, tmp.begin() + i + k);
        ListNode* res = new ListNode(NULL);
        ListNode* cur = res;
        for (int i = 0; i < tmp.size(); ++i) {
            cur->next = new ListNode(tmp[i]);
            cur = cur->next;
        }
        return res->next;
    }
};

