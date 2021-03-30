// 605. Can Place Flowers


// Runtime: 12 ms, faster than 91.13% of C++ online submissions for Can Place Flowers.
// Memory Usage: 20.3 MB, less than 61.98% of C++ online submissions for Can Place Flowers.
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int can_place = 0, // can place flower num
            con_plot = 0; // continue plot num
        for (int i = 0; i < flowerbed.size(); ++i) {
            if (flowerbed[i] == 0) {
                if (i == 0 || i == flowerbed.size() - 1) con_plot++;
                if (i == 0 && i == flowerbed.size() - 1) con_plot++;
                
                con_plot++;
            } else {
                can_place += (con_plot - 1) / 2;
                con_plot = 0;
            }
        }
        return n <= (can_place + (con_plot - 1) / 2);
    }
};
