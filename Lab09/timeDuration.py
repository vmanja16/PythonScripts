import re, glob, sys, os

class TimeSpan:
    def __init__(self, weeks, days, hours):
        if type(weeks) != int:
            raise TypeError("Class only accepts integers")
        if type(days) != int:
            raise TypeError("Class only accepts integers")
        if type(hours) != int:
            raise TypeError("Class only accepts integers")
        if weeks <0:
            raise ValueError("Values cannot be negative")
        if days <0:
            raise ValueError("Values cannot be negative")
        if hours <0:
            raise ValueError("Values cannot be negative")

        self.weeks = weeks
        self. hours = hours % 24
        self.days = days + int(hours/24)
        self.weeks += int(self.days/7)
        self.days = self.days % 7

    def __str__(self):
        return "{0:02d}W {1:01d}D {2:02d}H".format(self.weeks, self.days, self.hours)

    def getTotalHours(self):
        total = self.weeks * 7 * 24 + self.days * 24 + self.hours
        return total

    def __add__(self, other):
        if type(other) != TimeSpan:
            raise TypeError("TimeSpan instance expected")
        return TimeSpan(self.weeks + other.weeks, self.days + other.days, self.hours + other.hours)

    def __radd__(self, other):
        if type(other) != TimeSpan:
            raise TypeError("TimeSpan instance expected")
        return TimeSpan(self.weeks + other.weeks, self.days + other.days, self.hours + other.hours)

    def __mul__(self, other):
        if type(other) != int:
            raise TypeError("Integer expected")
        if other <= 0:
            raise ValueError("multiplicand must be greater than 0")
        return TimeSpan(self.weeks * other, self.days * other, self.hours * other)

    def __rmul__(self, other):
        if type(other) != int:
            raise TypeError("Integer expected")
        if other <= 0:
            raise ValueError("multiplicand must be greater than 0")
        return TimeSpan(self.weeks * other, self.days * other, self.hours * other)




