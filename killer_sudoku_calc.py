#! /usr/bin/env python3
"""
Killer Sudoku Calculator Function.

Generate summands based on their sum with single-digit number only.

Feature:
- exclusion of digits

Note: Summands is the number to be added
"""


def killer_sudoku_calc(sum, length=2, excl=None):
    if length > 9:
        return []

    excl = [] if not excl else excl

    # Base case: length < 2.
    if length < 2:
        # Check for single-digit condition and excluded digit here.
        if 1 <= sum <= 9 and sum not in excl:
            return [(sum,)]
        else:
            return []

    res = []
    for i in range(1, sum // length + 1):
        # skip number in exclude
        if i in excl:
            continue

        # add number to exlcude list
        excl.append(i)

        tmp = killer_sudoku_calc(sum - i, length - 1, excl)

        # remove recently added number
        excl.pop()

        for j in tmp:
            # make the tuple and append to res
            summands = (i,) + j
            res.append(summands)

    # Filter is needed for len > 3 because duplicates are unavoidable
    res = sorted(list(set(map(tuple, map(sorted, res)))))

    return res
