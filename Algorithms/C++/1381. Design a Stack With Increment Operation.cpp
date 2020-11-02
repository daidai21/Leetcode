// Runtime: 52 ms, faster than 88.67% of C++ online submissions for Design a Stack With Increment Operation.
// Memory Usage: 21.4 MB, less than 7.98% of C++ online submissions for Design a Stack With Increment Operation.
class CustomStack {
public:
    CustomStack(int maxSize) : max_size(maxSize) { }
    
    void push(int x) {
        if (stc.size() >= max_size)
            return;
        stc.push_back(x);
    }
    
    int pop() {
        int res = -1;
        if (stc.size() > 0) {
            res = stc[stc.size() - 1];
            stc.pop_back();
        }
        return res;
    }
    
    void increment(int k, int val) {
        k = min(max_size, k);
        k = min((int)stc.size(), k);
        for (int i = 0; i < k; ++i) {
            stc[i] += val;
        }
    }
private:
    int max_size;
    vector<int> stc;
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
