# Runtime: 152 ms, faster than 75.38% of Python3 online submissions for Lemonade Change.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Lemonade Change.
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0
        for bill in bills:
            # find change
            target = bill - 5
            if target >= 10 and tens > 0:
                tens -= 1
                target -= 10
            if fives >= target / 5:
                fives -= target / 5
            else:
                return False
            # add change
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
        return True
