// Runtime: 104 ms, faster than 89.18% of C++ online submissions for LRU Cache.
// Memory Usage: 38.1 MB, less than 78.05% of C++ online submissions for LRU Cache.
class LRUCache {
public:
    LRUCache(int capacity) : capacity(capacity) {}
    
    int get(int key) {
        auto it = hash.find(key);
        if (it == hash.end())
            return -1;
        cache.splice(cache.begin(), cache, it->second);
        return it->second->second;
    }
    
    void put(int key, int value) {
        auto it = hash.find(key);
        if (it != hash.end()) {
            it->second->second = value;
            return cache.splice(cache.begin(), cache, it->second);
        }
        cache.insert(cache.begin(), make_pair(key, value));
        hash[key] = cache.begin();
        if (cache.size() > capacity) {
            hash.erase(cache.back().first);
            cache.pop_back();
        }
    }
private:
    unordered_map<int, list<pair<int, int>>::iterator> hash;
    vector<pair<int, int>> mem;
    list<pair<int, int>> cache;
    int capacity;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
