// Runtime: 96 ms, faster than 83.28% of C++ online submissions for Design HashSet.
// Memory Usage: 76.6 MB, less than 33.33% of C++ online submissions for Design HashSet.
class MyHashSet {
public:
    /** Initialize your data structure here. */
    MyHashSet() {
        memset(arr, 0, 1000001);
    }
    
    void add(int key) {
        arr[key] = true;
    }
    
    void remove(int key) {
        arr[key] = false;
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        return arr[key];
    }
private:
    int arr[1000001];
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
