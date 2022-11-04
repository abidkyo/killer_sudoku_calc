#! /usr/bin/env python3
"""
Killer Sudoku Calculator Function.

Generate summands based on their sum with single-digit number only.

Feature:
- unlimited length of summands
- exclusion of digits

Note: Summands is the number to be added
"""


def killer_sudoku_calc(sum, len=2, excl=None, unique=False):
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

        if unique:
            excl.append(i)

        tmp = killer_sudoku_calc(sum - i, len - 1, excl, unique)

        if unique:
            excl.pop()

        for j in tmp:
            # make the tuple and append to res
            summands = (i,) + j
            res.append(summands)

    # Filter is needed for len > 3 because duplicates are unavoidable
    res = sorted(list(set(map(tuple, map(sorted, res)))))

    return res
