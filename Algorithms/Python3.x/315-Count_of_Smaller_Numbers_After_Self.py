class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort_(enum):
            mid = len(enum) // 2
            if mid:
                left, right = sort_(enum[:mid]), sort_(enum[mid:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort_(list(enumerate(nums)))
        return smaller
