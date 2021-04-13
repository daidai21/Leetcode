// 731. My Calendar II


// 一个是单次预定的所有时间
// 另一个列表将是肯定是重复预订的所有时间

// Runtime: 68 ms, faster than 97.37% of C++ online submissions for My Calendar II.
// Memory Usage: 33.9 MB, less than 81.18% of C++ online submissions for My Calendar II.
class MyCalendarTwo {
public:
    MyCalendarTwo() {}
    
    bool book(int start, int end) {
        for (pair<int, int> it : overlaps) {
            if (it.first < end && start < it.second) {
                return false;
            }
        }
        for (pair<int, int> it : calendar) {
            if (it.first < end && start < it.second) {
                overlaps.push_back({
                    max(start, it.first),
                    min(end, it.second)
                });
            }
        }
        calendar.push_back({start, end});
        return true;
    }
private:
    vector<pair<int, int>> calendar;
    vector<pair<int, int>> overlaps;

};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(start,end);
 */













// TreeMap
// Boundary Count 边界计数

// Runtime: 200 ms, faster than 46.42% of C++ online submissions for My Calendar II.
// Memory Usage: 38.7 MB, less than 47.93% of C++ online submissions for My Calendar II.

class MyCalendarTwo {
public:
    MyCalendarTwo() {}
    
    bool book(int start, int end) {
        mp[start]++;
        mp[end]--;
        int booked = 0;
        for (auto it = mp.begin(); it != mp.end(); ++it) {
            booked += it->second;
            if (booked > 2) {
                mp[start]--;
                mp[end]++;
                return false;
            }
        }
        return true;
    }

private:
    map<int, int> mp;

};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(start,end);
 */
