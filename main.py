#! /usr/bin/env python3
"""
Script to generate summands based on their sum.

Generate solution with single digit number only.

Limitation:
- Length of number is 2

Note: Summands is the number to be added
"""

import argparse
from summand_generator import summand_generator


# Create argument parser
parser = argparse.ArgumentParser(description="Summands Generator")
parser.add_argument("sum", type=int, help="Summation result")
args = parser.parse_args()

sum = args.sum


print(summand_generator(sum))
