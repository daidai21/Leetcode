# call lib
class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

# quick sort
class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        def sort_recursion(array, left, right):
            if left >= right: return  # 递归停止
            i, j = left, right
            flag = array[left]  # 取首位为对比标志值
            while i < j:  # 找flag的最终位置
                while i < j and array[j] >= flag:  # 用j向左扫描找小于flag的记录
                    j -= 1
                if i < j:
                    array[i] = array[j]  # 小记录移到左边
                    i += 1
                while i < j and array[i] <= flag:  # 用i向右扫描找大于flag的记录
                    i += 1
                if i < j:
                    array[j] = array[i]  # 大记录移到右边
                    j -= 1
            array[i] = flag  # 将对比的标志位存入其最终位置
            sort_recursion(array, left, i - 1)  # 左边
            sort_recursion(array, i + 1, right)  # 右边

        sort_recursion(nums, 0, len(nums) - 1)

