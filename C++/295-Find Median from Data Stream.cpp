class MedianFinder {
private:
    vector<int> vec;
public:
    /** initialize your data structure here. */
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if (vec.size() == 0) {
            vec.push_back(num);
        } else {
            int l = 0, r = vec.size() - 1;
            while (l <= r) {
                int mid = (l + r) / 2;
                if (num < vec[mid])
                    r = mid - 1;
                else
                    l = mid + 1;
            }
            vec.insert(vec.begin() + l, num);
        }
    }
    
    double findMedian() {
        int vec_size = vec.size();
        if (vec_size & 1)
            return vec[vec_size / 2];
        else
            return (vec[vec_size / 2 - 1] + vec[vec_size / 2]) * 0.5;
    }
};