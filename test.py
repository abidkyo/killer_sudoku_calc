#! /usr/bin/env python3
"""Test for Summand Generator Function."""


from summand_generator import summand_generator
import unittest


res_2numbers_repeating = [
    [],
    [],
    [(1, 1)],
    [(1, 2)],
    [(1, 3), (2, 2)],
    [(1, 4), (2, 3)],
    [(1, 5), (2, 4), (3, 3)],
    [(1, 6), (2, 5), (3, 4)],
    [(1, 7), (2, 6), (3, 5), (4, 4)],
    [(1, 8), (2, 7), (3, 6), (4, 5)],
    [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)],
    [(2, 9), (3, 8), (4, 7), (5, 6)],
    [(3, 9), (4, 8), (5, 7), (6, 6)],
    [(4, 9), (5, 8), (6, 7)],
    [(5, 9), (6, 8), (7, 7)],
    [(6, 9), (7, 8)],
    [(7, 9), (8, 8)],
    [(8, 9)],
    [(9, 9)],
    [],
    [],
]

res_3numbers_repeating = [
    [],
    [],
    [],
    [(1, 1, 1)],
    [(1, 1, 2)],
    [(1, 1, 3), (1, 2, 2)],
    [(1, 1, 4), (1, 2, 3), (2, 2, 2)],
    [(2, 2, 3), (1, 3, 3), (1, 1, 5), (1, 2, 4)],
    [(2, 3, 3), (1, 1, 6), (1, 3, 4), (2, 2, 4), (1, 2, 5)],
    [(1, 4, 4), (1, 3, 5), (1, 2, 6), (2, 2, 5), (3, 3, 3), (2, 3, 4), (1, 1, 7)],
    [(1, 2, 7), (2, 2, 6), (3, 3, 4), (2, 3, 5), (2, 4, 4), (1, 1, 8), (1, 3, 6), (1, 4, 5)],
    [(2, 4, 5), (2, 3, 6), (1, 1, 9), (1, 4, 6), (1, 3, 7), (2, 2, 7), (3, 3, 5), (1, 2, 8), (3, 4, 4), (1, 5, 5)],
    [
        (1, 3, 8),
        (2, 5, 5),
        (1, 4, 7),
        (1, 2, 9),
        (2, 2, 8),
        (1, 5, 6),
        (3, 3, 6),
        (4, 4, 4),
        (3, 4, 5),
        (2, 3, 7),
        (2, 4, 6),
    ],
    [
        (2, 2, 9),
        (3, 4, 6),
        (1, 5, 7),
        (3, 3, 7),
        (1, 6, 6),
        (4, 4, 5),
        (2, 4, 7),
        (2, 3, 8),
        (3, 5, 5),
        (1, 3, 9),
        (2, 5, 6),
        (1, 4, 8),
    ],
    [
        (2, 3, 9),
        (2, 4, 8),
        (2, 6, 6),
        (3, 5, 6),
        (4, 5, 5),
        (2, 5, 7),
        (1, 4, 9),
        (4, 4, 6),
        (1, 5, 8),
        (3, 3, 8),
        (1, 6, 7),
        (3, 4, 7),
    ],
    [
        (2, 6, 7),
        (3, 5, 7),
        (5, 5, 5),
        (2, 5, 8),
        (3, 6, 6),
        (1, 7, 7),
        (3, 4, 8),
        (1, 5, 9),
        (3, 3, 9),
        (1, 6, 8),
        (4, 5, 6),
        (2, 4, 9),
        (4, 4, 7),
    ],
    [
        (1, 7, 8),
        (4, 6, 6),
        (3, 6, 7),
        (4, 4, 8),
        (1, 6, 9),
        (3, 4, 9),
        (4, 5, 7),
        (3, 5, 8),
        (2, 7, 7),
        (2, 6, 8),
        (2, 5, 9),
        (5, 5, 6),
    ],
    [
        (4, 5, 8),
        (1, 8, 8),
        (3, 7, 7),
        (2, 6, 9),
        (3, 5, 9),
        (2, 7, 8),
        (4, 6, 7),
        (5, 5, 7),
        (3, 6, 8),
        (1, 7, 9),
        (5, 6, 6),
        (4, 4, 9),
    ],
    [
        (2, 7, 9),
        (6, 6, 6),
        (5, 5, 8),
        (4, 6, 8),
        (4, 7, 7),
        (3, 6, 9),
        (5, 6, 7),
        (2, 8, 8),
        (4, 5, 9),
        (3, 7, 8),
        (1, 8, 9),
    ],
    [(5, 5, 9), (2, 8, 9), (4, 6, 9), (4, 7, 8), (5, 6, 8), (1, 9, 9), (3, 7, 9), (5, 7, 7), (6, 6, 7), (3, 8, 8)],
    [(5, 6, 9), (4, 8, 8), (5, 7, 8), (6, 6, 8), (3, 8, 9), (6, 7, 7), (2, 9, 9), (4, 7, 9)],
    [(5, 7, 9), (3, 9, 9), (7, 7, 7), (5, 8, 8), (6, 7, 8), (4, 8, 9), (6, 6, 9)],
    [(5, 8, 9), (6, 7, 9), (7, 7, 8), (4, 9, 9), (6, 8, 8)],
    [(6, 8, 9), (5, 9, 9), (7, 7, 9), (7, 8, 8)],
    [(7, 8, 9), (6, 9, 9), (8, 8, 8)],
    [(8, 8, 9), (7, 9, 9)],
    [(8, 9, 9)],
    [(9, 9, 9)],
    [],
    [],
    [],
]


class TestSummand2Number(unittest.TestCase):
    def test_repeating(self):
        for i in range(0, len(res_2numbers_repeating)):
            res = summand_generator(i)
            self.assertCountEqual(res, res_2numbers_repeating[i])


class TestSummand3Number(unittest.TestCase):
    def test_repeating(self):
        for i in range(0, len(res_3numbers_repeating)):
            res = summand_generator(i, 3)
            self.assertCountEqual(res, res_3numbers_repeating[i])


if __name__ == "__main__":
    unittest.main()
