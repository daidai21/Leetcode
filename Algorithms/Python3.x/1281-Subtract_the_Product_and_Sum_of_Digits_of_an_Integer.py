class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, add = 1, 0
        for i in str(n):
            product *= int(i)
            add += int(i)
        return product - add
