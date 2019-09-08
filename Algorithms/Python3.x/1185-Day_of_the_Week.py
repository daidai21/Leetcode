# Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Day of the Week.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Day of the Week.
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        months = [
                    0,   # 0 None
                    31,  # 1
                    28,  # 2
                    31,  # 3
                    30,  # 4
                    31,  # 5
                    30,  # 6
                    31,  # 7
                    31,  # 8
                    30,  # 9
                    31,  # 10
                    30,  # 11
                    31,  # 12
                ]
        days = 5
        # add every year
        for i in range(1971, year):
            if self.is_leap_year(i):
                days += 366 % 7
            else:
                days += 365 % 7
        # add every month
        for i in range(1, month):
            if i == 2:
                if self.is_leap_year(year):
                    days += months[i] + 1
            days += months[i]
        # add day
        days += day - 1
        days %= 7
        return week[days]

    def is_leap_year(self, year):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


# Runtime: 40 ms, faster than 50.00% of Python3 online submissions for Day of the Week.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Day of the Week.
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        from datetime import datetime
        return datetime(year, month, day).strftime("%A")
