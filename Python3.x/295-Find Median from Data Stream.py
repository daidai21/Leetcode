class MedianFinder:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.lst, num)

    def findMedian(self) -> float:
        len_lst = len(self.lst)
        if len_lst % 2 == 1:
            return self.lst[len_lst // 2]
        else:
            return (self.lst[len_lst // 2 - 1] + self.lst[len_lst // 2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()




# binary search insert
class MedianFinder:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []

    def addNum(self, num: int) -> None:
        if len(self.lst) == 0 or self.lst[-1] < num:
            self.lst.append(num)
            return
        left, right = 0, len(self.lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if num < self.lst[mid]:
                right = mid - 1
            else:
                left = mid + 1
        self.lst.insert(left, num)

    def findMedian(self) -> float:
        len_lst = len(self.lst)
        if len_lst % 2 == 1:
            return self.lst[len_lst // 2]
        else:
            return (self.lst[len_lst // 2 - 1] + self.lst[len_lst // 2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()