from typing import List


################################################################################
# error
################################################################################
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        for idx, val in enumerate(deck):
            deck[val] = -deck[val]
        for idx, val in enumerate(deck):
            if val <= 0:
                return False
        return True


################################################################################
# error: set visited
################################################################################
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        vis = set()
        for idx, val in enumerate(deck):
            if val in vis:
                vis.remove(val)
            else:
                vis.add(val)
        return len(vis) == 0


# Runtime: 144 ms, faster than 50.19% of Python3 online submissions for X of a Kind in a Deck of Cards.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for X of a Kind in a Deck of Cards.
################################################################################
# gcd
################################################################################
from collections import Counter
from functools import reduce
# from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        gcd = lambda x, y: gcd(y, x % y) if y > 0 else x
        return reduce(gcd, Counter(deck).values()) > 1


print(Solution().hasGroupsSizeX([1,2,3,4,4,3,2,1]))  # true
print(Solution().hasGroupsSizeX([1,1,1,2,2,2,3,3]))  # false
print(Solution().hasGroupsSizeX([1]))  # false
print(Solution().hasGroupsSizeX([1,1]))  # true
print(Solution().hasGroupsSizeX([1,1,2,2,2,2]))  # true
print(Solution().hasGroupsSizeX([0,0,0,1,1,1,2,2,2]))  # true
