# Runtime: 40 ms, faster than 61.72% of Python3 online submissions for Integer to English Words.
# Memory Usage: 13.9 MB, less than 8.70% of Python3 online submissions for Integer to English Words.
class Solution:
    def numberToWords(self, num: int) -> str:
        return "Zero" if num == 0 else self.recursion(num)

    def recursion(self, num):
        below_ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        below_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        below_hundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        res = ""
        if num < 10:
            res = below_ten[num]
        elif num < 20:
            res = below_twenty[num % 10]
        elif num < 100:
            res = below_hundred[num // 10] + ' ' + below_ten[num % 10]
        elif num < 1000:
            res = below_ten[num // 100] + " Hundred " + self.recursion(num % 100)
        elif num < 1000000:
            res = self.recursion(num // 1000) + " Thousand " + self.recursion(num % 1000)
        elif num < 1000000000:
            res = self.recursion(num // 1000000) + " Million " + self.recursion(num % 1000000)
        else:
            res = self.recursion(num // 1000000000) + " Billion " + self.recursion(num % 1000000000)
        return res.strip()
