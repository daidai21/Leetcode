// Runtime: 2 ms, faster than 77.52% of Java online submissions for Add Two Numbers.
// Memory Usage: 39.2 MB, less than 82.91% of Java online submissions for Add Two Numbers.
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode();
        ListNode tmp = res;
        boolean flag = false;
        while (l1 != null || l2 != null || flag) {
            int add = (l1 != null ? l1.val : 0) + (l2 != null ? l2.val : 0) + (flag ? 1 : 0);
            flag = add >= 10;
            tmp.next = new ListNode(add % 10);
            tmp = tmp.next;
            l1 = l1 != null ? l1.next : null;
            l2 = l2 != null ? l2.next : null;
        }
        return res.next;
    }
}
