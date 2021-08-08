// Runtime: 64 ms, faster than 65.21% of C++ online submissions for Sort an Array.
// Memory Usage: 12.5 MB, less than 97.22% of C++ online submissions for Sort an Array.
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums;
    }
};

// 快排
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        quickSort(nums, 0, nums.size() - 1);
        return nums;
    }

private:
    void quickSort(std::vector<int>& nums, int left, int right) {
        if (left >= right) return;
        int mid = partition(nums, left, right);
        quickSort(nums, left, mid - 1);
        quickSort(nums, mid + 1, right);
    }

    int partition(std::vector<int>& nums, int left, int right) {
        int i = left + 1,
            j = right;
        while (true) {
            while (i <= j && nums[i] <= nums[left]) i++;
            while (i <= j && nums[left] <= nums[j]) j--;
            if (i > j) break;
            std::swap(nums[i], nums[j]);
        }
        std::swap(nums[j], nums[left]);
        return j;
    }
};


// 归并排序
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        mergeSort(nums, 0, nums.size() - 1);
        return nums;
    }

private:
    void mergeSort(std::vector<int>& nums, int left, int right) {
        if (left >= right) {
            return ;
        }
        int mid = left + (right - left) / 2;
        mergeSort(nums, left, mid);
        mergeSort(nums, mid + 1, right);
        merge(nums, left, mid, right);
    }

    void merge(std::vector<int>& nums, int left, int mid, int right) {
        std::vector<int> tmp(right - left + 1);
        int i = left,
            j = mid + 1,
            k = 0;
        while (i <= mid && j <= right) {
            if (nums[i] < nums[j]) {
                tmp[k] = nums[i];
                k++;
                i++;
            } else {
                tmp[k] = nums[j];
                k++;
                j++;
            }
        }
        while (i <= mid) {
            tmp[k] = nums[i];
            k++;
            i++;
        }
        while (j <= right) {
            tmp[k] = nums[j];
            k++;
            j++;
        }
        for (i = 0; i < k; ++i) {
            nums[left + i] = tmp[i];
        }
    }
};

// 堆排序
// 堆排序的思想就是先将待排序的序列建成大根堆，使得每个父节点的元素大于等于它的子节点。此时整个序列最大值即为堆顶元素，我们将其与末尾元素交换，使末尾元素为最大值，然后再调整堆顶元素使得剩下的 n-1n−1 个元素仍为大根堆，再重复执行以上操作我们即能得到一个有序的序列。
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        // 建堆阶段 （自底向上的方法）
        for (int i = nums.size() / 2 - 1; i >= 0; --i) {
            siftDown(nums, nums.size(), i);
        }
        // 排序阶段
        for (int i = nums.size() - 1; i > 0; --i){
            std::swap(nums[0], nums[i]);
            siftDown(nums, i, 0);
        }
        return nums;
    }

private:
    // 筛选下来
    void siftDown(std::vector<int>& nums, int n, int i) {
        int biggest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (left < n && nums[biggest] < nums[left]) {
            biggest = left;
        }
        if (right < n && nums[biggest] < nums[right]) {
            biggest = right;
        }
        if (biggest != i) {
            std::swap(nums[i], nums[biggest]);
            siftDown(nums, n, biggest);
        }
    }
};
