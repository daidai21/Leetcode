// Runtime: 76 ms, faster than 91.09% of C++ online submissions for Subrectangle Queries.
// Memory Usage: 18.8 MB, less than 66.67% of C++ online submissions for Subrectangle Queries.
class SubrectangleQueries {
public:
    SubrectangleQueries(vector<vector<int>>& rectangle) {
        this->rectangle = rectangle;
    }
    
    void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        for (int row = row1; row <= row2; ++row) {
            for (int col = col1; col <= col2; ++col) {
                this->rectangle[row][col] = newValue;
            }
        }
    }
    
    int getValue(int row, int col) {
        return this->rectangle[row][col];
    }
private:
    vector<vector<int>> rectangle;
};

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * SubrectangleQueries* obj = new SubrectangleQueries(rectangle);
 * obj->updateSubrectangle(row1,col1,row2,col2,newValue);
 * int param_2 = obj->getValue(row,col);
 */
