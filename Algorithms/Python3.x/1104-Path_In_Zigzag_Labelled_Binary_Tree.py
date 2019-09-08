# Runtime: 48 ms, faster than 21.99% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        while label:  # This loop get a normal binary tree result.
            res.append(label)
            label = label // 2
        res = res[::-1]  # Then using this formula: complement = 2 ** (height + 1) + 2 ** height - item
        for i in range(len(res) - 2, 0, -2):
            res[i] = 2 ** (i + 1) - 1 + 2 ** i - res[i]
        return res
