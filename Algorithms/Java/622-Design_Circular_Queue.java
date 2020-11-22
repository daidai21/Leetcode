// Runtime: 4 ms, faster than 93.91% of Java online submissions for Design Circular Queue.
// Memory Usage: 39.6 MB, less than 62.04% of Java online submissions for Design Circular Queue.
class MyCircularQueue {
    private int[] arr;
    private int front = 0;
    private int rear = -1;
    private int len = 0; // filled length

    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        arr = new int[k];
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }
        rear = (rear + 1) % arr.length;
        len++;
        arr[rear] = value;
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }
        front = (front + 1) % arr.length;
        len--;
        return true;
    }
    
    /** Get the front item from the queue. */
    public int Front() {
        return isEmpty() ? -1 : arr[front];
    }
    
    /** Get the last item from the queue. */
    public int Rear() {
        return isEmpty() ? -1 : arr[rear];
    }
    
    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
        return len == 0;
    }
    
    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
        return arr.length == len;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
