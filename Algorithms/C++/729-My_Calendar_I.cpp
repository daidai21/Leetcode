// 729. My Calendar I

// Runtime: 100 ms, faster than 33.97% of C++ online submissions for My Calendar I.
// Memory Usage: 37.7 MB, less than 88.82% of C++ online submissions for My Calendar I.
class MyCalendar {
public:
    MyCalendar() { }
    
    bool book(int start, int end) {
        for (pair<int, int> p : lst)
            if (max(p.first, start) < min(end, p.second)) return false;
        lst.push_back(make_pair(start, end));
        return true;
    }
    
private:
    vector<pair<int, int>> lst;
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */



// TreeMap
// Runtime: 72 ms, faster than 95.25% of C++ online submissions for My Calendar I.
// Memory Usage: 38.9 MB, less than 36.68% of C++ online submissions for My Calendar I.
class MyCalendar {
public:
    MyCalendar() { }
    
    bool book(int start, int end) {
        auto nxt = events.upper_bound(start);
        if (nxt != events.end() && (*nxt).second < end) return false;
        events.insert({end, start});
        return true;
    }
    
private:
    map<int, int> events;
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */
