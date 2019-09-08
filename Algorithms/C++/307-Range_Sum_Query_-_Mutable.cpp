// Runtime: 144 ms, faster than 24.61% of C++ online submissions for Range Sum Query - Mutable.
// Memory Usage: 18.8 MB, less than 99.23% of C++ online submissions for Range Sum Query - Mutable.
class NumArray {
public:
    NumArray(vector<int>& nums) {
        vec.swap(nums);
    }
    
    void update(int i, int val) {
        vec[i] = val;
    }
    
    int sumRange(int i, int j) {
        int res = 0;
        for (; i <= j; ++i)
            res += vec[i];
        return res;
    }
private:
    vector<int> vec;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(i,val);
 * int param_2 = obj->sumRange(i,j);
 */