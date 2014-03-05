"""
1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,

Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class ModCounter(object):
    def __init__(self, mod, start=0):
        self.mod = mod
        self.counter = start
        self.loop = self.inc()

    def inc(self):
        while 1:
            yield self.counter
            self.counter = (self.counter + 1) % self.mod


def run():
    total_sundays = 0
    mod_sunday = ModCounter(7, 2)    # 1/1/1901 was a tuesday
    year = 1901

    while year < 2001:
        if year % 4 == 0:
            months[1] = 29
        else:
            months[1] = 28

        for month in range(12):
            for day in range(months[month]):
                mod_sunday.loop.next()
                if day == 0:
                    if mod_sunday.counter == 0:
                        total_sundays += 1

        year += 1

    print total_sundays

run()
