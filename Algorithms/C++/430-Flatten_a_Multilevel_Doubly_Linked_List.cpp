// stack
// Runtime: 8 ms, faster than 97.89% of C++ online submissions for Flatten a Multilevel Doubly Linked List.
// Memory Usage: 9.8 MB, less than 100.00% of C++ online submissions for Flatten a Multilevel Doubly Linked List.

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/
class Solution {
public:
    Node* flatten(Node* head) {
        if (head == nullptr)
            return nullptr;
        Node* dummy = new Node();
        stack<Node*> stk;
        stk.push(head);
        Node* prev = dummy;
        while (!stk.empty()) {
            Node* temp = stk.top();
            stk.pop();
            temp->prev = prev;
            prev->next = temp;
            if (temp->next != nullptr) {
                stk.push(temp->next);
                temp->next = NULL;
            }
            if (temp->child != nullptr) {
                stk.push(temp->child);
                temp->child = NULL;
            }
            prev = temp;
        }
        dummy->next->prev = nullptr;
        return dummy->next;
    }
};
