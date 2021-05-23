class Solution {
public:
    int minSpeedOnTime(vector<int>& dist, double hour) {
        if (dist.size() > std::ceil(hour)) {
            return -1;
        }
        // binary search
        int maxSpeed = std::numeric_limits<int>::max();
        int minSpeed = 1;
        while (maxSpeed > minSpeed) {
            int mid = (maxSpeed - minSpeed) / 2 + minSpeed;
            if (arriveOnTime(dist, hour, mid)) {
                maxSpeed = mid;
            } else {
                minSpeed = mid + 1;
            }
        }
        return maxSpeed;
    }
    
private:
    bool arriveOnTime(const std::vector<int>& dist, double hour, int speed) {
        double costHour = 0;
        for (int i = 0; i < dist.size(); ++i) {
            if (i == dist.size() - 1) {
                costHour += (double) dist[i] / speed;
            } else {
                costHour += std::ceil((double) dist[i] / speed);                
            }
        }
        return costHour <= hour;
    }
};
