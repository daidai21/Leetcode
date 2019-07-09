class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        for i, v in enumerate(values):
            res += (num // values[i]) * numerals[i]
            num %= values[i]
        return res