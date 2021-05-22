// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Self Crossing.
// Memory Usage: 6.9 MB, less than 55.84% of C++ online submissions for Self Crossing.

/*               i-2
    case 1 : i-1┌─┐
                └─┼─>i
                 i-3
                 
                    i-2
    case 2 : i-1 ┌────┐
                 └─══>┘i-3
                 i  i-4      (i overlapped i-4)

    case 3 :    i-4
               ┌──┐ 
               │i<┼─┐
            i-3│ i-5│i-1
               └────┘
                i-2

*/
class Solution {
 public:
  bool isSelfCrossing(vector<int>& distance) {
    for (int i = 3; i < distance.size(); ++i) {
      // Case 1:
      if (distance[i] >= distance[i - 2] && distance[i - 1] <= distance[i - 3]) {
        return true;
      }
      // Case 2:
      if (i >= 4 && distance[i - 1] == distance[i - 3] && distance[i] + distance[i - 4] >= distance[i - 2]) {
        return true;
      }
      // Case 3:
      if (i >= 5 && distance[i - 2] >= distance[i - 4] && distance[i] + distance[i - 4] >= distance[i - 2] && distance[i - 1] <= distance[i - 3] && distance[i - 1] + distance[i - 5] >= distance[i - 3]) {
        return true;
      }
    }
    return false;
  }
};
