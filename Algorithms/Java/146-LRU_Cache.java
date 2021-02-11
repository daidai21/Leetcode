// Runtime: 142 ms, faster than 8.29% of Java online submissions for LRU Cache.
// Memory Usage: 47.9 MB, less than 24.40% of Java online submissions for LRU Cache.
class LRUCache {
    public LRUCache(int capacity) {
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if (map.containsKey(key)) {
            queue.remove(key);
            queue.add(key);
            return map.get(key);
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (!map.containsKey(key) && map.size() == capacity) {
            map.remove(queue.remove());
        }
        if (map.containsKey(key)) {
            queue.remove(key);
        }
        map.put(key, value);
        queue.add(key);
    }
    
    private Queue<Integer> queue = new LinkedList<Integer>();
    private HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    private int capacity;
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
