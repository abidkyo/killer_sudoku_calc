#! /usr/bin/env python3
"""
Script to generate summands based on their sum.

Generate solution with single digit number only.

Feature:
- unlimited length of summands
- exclusion of digits

Note: Summands is the number to be added
"""

import argparse
from summand_generator import summand_generator


# Create argument parser
parser = argparse.ArgumentParser(description="Summands Generator")
parser.add_argument("sum", type=int, help="Summation result")
parser.add_argument("-l", "--length", default=2, type=int, help="Length of summands")
parser.add_argument("-e", "--exclude", default=None, nargs="+", type=int, help="Digit to exclude")
parser.add_argument("-u", "--unique", action="store_true", help="Unique digit (no repeat)")
args = parser.parse_args()

sum = args.sum
length = args.length
exclude = args.exclude
unique = args.unique


print(summand_generator(sum, length, exclude, unique))
