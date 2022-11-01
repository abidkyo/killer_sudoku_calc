#! /usr/bin/env python3
"""Summand Generator Function."""


def summand_generator(sum, len=2):
    res = []
    for i in range(1, sum // 2 + 1):
        j = sum - i

        # make the tuple and append to res
        # if number between 1 and 9 and the tuple not yet in res
        summands = (i, j)
        if 1 <= j <= 9 and summands not in res:
            res.append(summands)

    return res
