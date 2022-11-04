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


print(killer_sudoku_calc(sum, length=length, excl=exclude, incl=include))
