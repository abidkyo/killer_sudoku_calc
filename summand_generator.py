#! /usr/bin/env python3
"""Summand Generator Function."""


def summand_generator(sum, len=2, excl=None):
    excl = [] if not excl else excl

    # Base case: length < 2.
    if len < 2:
        # Check for single-digit condition and excluded digit here.
        if 1 <= sum <= 9 and sum not in excl:
            return [(sum,)]
        else:
            return []

    res = []
    for i in range(1, sum // len + 1):
        # skip number in exclude
        if i in excl:
            continue

        tmp = summand_generator(sum - i, len - 1, excl)

        for j in tmp:
            # make the tuple and append to res
            summands = (i,) + j
            res.append(summands)

    # Filter is needed for len > 3 because duplicates are unavoidable
    res = list(set(map(tuple, map(sorted, res))))

    return res
