// Runtime: 96 ms, faster than 54.76% of C++ online submissions for Design Parking System.
// Memory Usage: 33.5 MB, less than 6.31% of C++ online submissions for Design Parking System.
class ParkingSystem {
public:
    ParkingSystem(int big, int medium, int small) {
        bi = big;
        me = medium;
        sm = small;
    }
    
    bool addCar(int carType) {
        if (carType == 1 && bi > 0) {
            bi--;
            return true;
        } else if (carType == 2 && me > 0) {
            me--;
            return true;
        } else if (carType == 3 && sm > 0) {
            sm--;
            return true;
        } else
            return false;
    }
private:
    int bi,
        me,
        sm;
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */
