#! /usr/bin/env python3.4
#
from listmod import find_median
l1 = input("Enter the first list of numbers: ")
l2 = input("Enter the second list of numbers: ")
l1 = [int(x) for x in l1.split()]
l2 = [int(x) for x in l2.split()]
(median, sorted_list) = find_median(l1,l2)

print("First list:", l1)
print("Second list:", l2)
print("Merged List:", sorted_list)
print("Median:", median)
