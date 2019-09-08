class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map<int, int> m;
        for (int num : nums) {
            if (m.count(num))
                m[num]++;
            else
                m[num] = 1;
        }
        map<int, int>::iterator it;
        int res = 0;
        for (it = m.begin(); it != m.end(); ++it) {
            if ((*it).second == 1)
                res = (*it).first;
        }
        return res;
    }
};


class Solution {
public:
    int singleNumber(vector<int>& nums) {
        vector<int> tmp;
        for (int num : nums) {
            bool flag = true;
            for (vector<int>::iterator it = tmp.begin(); it != tmp.end(); ++it) {
                if (*it == num) {
                    tmp.erase(it);
                    flag = false;
                    break;
                }
            }
            if (flag)
                tmp.push_back(num);
        }
        return tmp[0];
    }
};
