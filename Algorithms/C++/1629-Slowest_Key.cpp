class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        char res;
        int max_key = 0;
        for (int i = 0; i < releaseTimes.size(); ++i) {
            if (i == 0) {
                if (max_key <= releaseTimes[i]) {
                    max_key = releaseTimes[i];
                    res = keysPressed[i];
                }
            } else {
                if (max_key <= releaseTimes[i] - releaseTimes[i - 1]) {
                    max_key = releaseTimes[i] - releaseTimes[i - 1];
                    res = keysPressed[i];
                }
            }
        }
        return res;
    }
};
