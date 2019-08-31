# Runtime: 32 ms, faster than 89.31% of Python3 online submissions for Water and Jug Problem.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Water and Jug Problem.
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return z == 0 or (x + y >= z and z % self.gcd(x, y) == 0)

    def gcd(self, x, y):  # greatest common divisor
        return x if y == 0 else self.gcd(y, x % y)


"""
z = m * x + n * y


# 辗转相除法: gcd(a, b) = gcd(b, a mod b)
(1)充分性：
设g是a,b的公约数，则a,b可由g来表示：
a = xg, b = yg (x,y为整数)
又，a可由b表示（任意一个数都可以由另一个数来表示）：
a = kb + r (k为整数，r为a除以b所得余数)
=> r = a - kb = xg - kyg = (x - ky)g
即，g也是r的约数。
这样，g就是(b, r)即(b, a mod b)的公约数。
(2)必要性：
设g是(b, a mod b)的公约数，类似于(1)，同样可以推出g也是(a, b)的公约数。
"""
