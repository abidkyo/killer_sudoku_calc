#! /usr/bin/env python3
"""
Script to use Killer Sudoku Calculator Function.

Generate summands based on their sum with single-digit number only.

Feature:
- exclusion of digits
- inclusion of digits

Note: Summands is the number to be added
"""

import argparse
from collections import Counter

from killer_sudoku_calc import killer_sudoku_calc


# Create argument parser
parser = argparse.ArgumentParser(description="Killer Sudoku Calculator")
parser.add_argument("sum", type=int, help="Sum of the cage")
parser.add_argument("-l", "--length", default=2, choices=range(2, 10), type=int, help="Size of the cage")
parser.add_argument("-e", "--exclude", default=None, nargs="+", type=int, help="Digits to exclude")
parser.add_argument("-i", "--include", default=None, nargs="+", type=int, help="Digits to include")
args = parser.parse_args()

sum = args.sum
length = args.length
exclude = args.exclude
include = args.include


res = killer_sudoku_calc(sum, length=length, excl=exclude, incl=include)
counter = Counter(sorted(x for t in res for x in t))

unique = []
common = []
for k, v in counter.items():
    if v == len(res):
        common.append(k)

    if v == 1:
        unique.append(k)


print(f"No. of Combinations : {len(res)}")
print(f"Combinations        : {res}")
print()
print(f"Digits              : {list(counter.keys())}")
print()
print(f"Unique              : {unique}")
print(f"Common              : {common}")
