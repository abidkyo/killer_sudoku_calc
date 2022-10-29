#! /usr/bin/env python3
"""Test for Summand Generator Function."""


from summand_generator import summand_generator
import unittest


res_2numbers = [
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


class TestSummand2Number(unittest.TestCase):
    def test(self):
        for i in range(0, len(res_2numbers)):
            res = summand_generator(i)
            self.assertCountEqual(res, res_2numbers[i])


if __name__ == "__main__":
    unittest.main()
