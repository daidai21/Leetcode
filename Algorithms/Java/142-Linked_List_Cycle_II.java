/**
 * 起点 到 环起点 为 a
 * 环起点 到 相遇点 为 b
 * 相遇点 到 环起点 为 c
 * 
 * 快指针走了 a + b + c + b
 * 慢指针走了 a + b
 * a + b + c + b = 2 * (a + b)
 * 所以 c == a
 */
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null) return null;
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {
                while (head != slow) {
                    head = head.next;
                    slow = slow.next;
                }
                return head;
            }
        }
        return null;
    }
}
