#! /usr/bin/env python3
"""Test for Summand Generator Function."""


from killer_sudoku_calc import killer_sudoku_calc
import unittest


res_2numbers = [
    [],
    [],
    [],
    [(1, 2)],
    [(1, 3)],
    [(1, 4), (2, 3)],
    [(1, 5), (2, 4)],
    [(1, 6), (2, 5), (3, 4)],
    [(1, 7), (2, 6), (3, 5)],
    [(1, 8), (2, 7), (3, 6), (4, 5)],
    [(1, 9), (2, 8), (3, 7), (4, 6)],
    [(2, 9), (3, 8), (4, 7), (5, 6)],
    [(3, 9), (4, 8), (5, 7)],
    [(4, 9), (5, 8), (6, 7)],
    [(5, 9), (6, 8)],
    [(6, 9), (7, 8)],
    [(7, 9)],
    [(8, 9)],
    [],
    [],
    [],
]

res_3numbers = [
    [],
    [],
    [],
    [],
    [],
    [],
    [(1, 2, 3)],
    [(1, 2, 4)],
    [(1, 3, 4), (1, 2, 5)],
    [(1, 3, 5), (1, 2, 6), (2, 3, 4)],
    [(1, 2, 7), (2, 3, 5), (1, 3, 6), (1, 4, 5)],
    [(2, 4, 5), (2, 3, 6), (1, 4, 6), (1, 3, 7), (1, 2, 8)],
]


class TestSummand2Number(unittest.TestCase):
    def test(self):
        for i in range(0, len(res_2numbers)):
            res = killer_sudoku_calc(i, length=2)
            self.assertCountEqual(res, res_2numbers[i])

    def test_exclusion(self):
        self.assertCountEqual(killer_sudoku_calc(7, length=2, excl=[5]), [(1, 6), (3, 4)])
        self.assertCountEqual(killer_sudoku_calc(8, length=2, excl=[3]), [(1, 7), (2, 6)])
        self.assertCountEqual(killer_sudoku_calc(9, length=2, excl=[2]), [(1, 8), (3, 6), (4, 5)])
        self.assertCountEqual(killer_sudoku_calc(10, length=2, excl=[1]), [(2, 8), (3, 7), (4, 6)])


class TestSummand3Number(unittest.TestCase):
    def test(self):
        for i in range(0, len(res_3numbers)):
            res = killer_sudoku_calc(i, length=3)
            self.assertCountEqual(res, res_3numbers[i])

    def test_inclusion(self):
        self.assertCountEqual(killer_sudoku_calc(9, length=3, incl=[2]), [(1, 2, 6), (2, 3, 4)])
        self.assertCountEqual(killer_sudoku_calc(10, length=3, incl=[3]), [(2, 3, 5), (1, 3, 6)])
        self.assertCountEqual(killer_sudoku_calc(11, length=3, incl=[8]), [(1, 2, 8)])


if __name__ == "__main__":
    unittest.main()
