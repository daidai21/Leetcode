class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> tmp;
        int i = 0, j = 0, k = 0;
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] < nums2[j]) {
                tmp.push_back(nums1[i]);
                i++;
                k++;
            } else {
                tmp.push_back(nums2[j]);
                j++;
                k++;
            }
        }
        while (i < nums1.size()) {
            tmp.push_back(nums1[i]);
            i++;
            k++;
        }
        while (j < nums2.size()) {
            tmp.push_back(nums2[j]);
            j++;
            k++;
        }
        if (k % 2 == 0)
            return (tmp[k / 2 - 1] + tmp[k / 2]) / 2.0;
        else
            return tmp[k / 2];
    }
};


class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        double res = 0;
        int i = 0, j = 0, k = 0;
        int stop = (nums1.size() + nums2.size()) / 2 - 1;  // the first stop index
        bool len_is_even = (nums1.size() + nums2.size()) % 2 == 0;
        while ((i < nums1.size() || j < nums2.size())) {
            if (i < nums1.size() && j < nums1.size()) {
                if (nums1[i] < nums2[j]) {
                    ++i; ++k;
                } else {
                    ++j; ++k;
                }
            } else if (i < nums1.size()) {
                ++i; ++k;
            } else {
                ++j; ++k;
            }
            if (k == stop || k == stop + 1) {
                res += max(nums1[i - 1], nums2[j - 1]);
                if (len_is_even && k == stop + 1) {
                    res += max(nums1[i - 1], nums2[j - 1]);
                    return res / 2.0;
                } else
                    return res;
            }
        }
    }
};