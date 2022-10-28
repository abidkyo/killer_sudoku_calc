#! /usr/bin/env python3
"""
Script to generate summands based on their sum.

Generate solution with single digit number only.

Limitation:
- Length of number is 2

Note: Summands is the number to be added
"""

import argparse

# Create argument parser
parser = argparse.ArgumentParser(description="Summands Generator")
parser.add_argument("sum", type=int, help="Summation result")
args = parser.parse_args()

sum = args.sum


def summand_generator(sum):
    res = []
    for i in range(1, 10):
        j = sum - i

        # make the tuple and append to res
        # if number between 1 and 9 and the tuple not yet in res
        summands = (i, j)
        if 1 <= j <= 9 and summands not in res:
            res.append(summands)

    # filter duplicates
    res = list(set(map(tuple, map(sorted, res))))
    return res


print(summand_generator(sum))
