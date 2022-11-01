#! /usr/bin/env python3
"""Summand Generator Function."""


def summand_generator(sum, len=2):
    # Base case: length < 2.
    if len < 2:
        # Check for single-digit condition here.
        if 1 <= sum <= 9:
            return [(sum,)]
        else:
            return []

    res = []
    for i in range(1, sum // len + 1):
        tmp = summand_generator(sum - i, len - 1)

        for j in tmp:
            # make the tuple and append to res
            # if the tuple not yet in res
            summands = (i,) + j
            if summands not in res:
                res.append(summands)

    # Filter is needed for len > 3 because duplicates are unavoidable
    res = list(set(map(tuple, map(sorted, res))))

    return res
