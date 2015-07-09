# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:26:14 2015

@author: jack
"""
import unittest

from tick_series import TickSeries

class TestTickSeries(unittest.TestCase):
    def test_number_of_ticks(self):
        series = TickSeries((0,1), 10)
        self.assertEqual(11, len(set(series.ticks)))

    def test_tick_values(self):
        series = TickSeries((0,1), 10)
        expected = [x / 10.0 for x in range(0, 11)]
        matched = zip(expected, series.ticks)
        for a, b in matched:
            self.assertAlmostEqual(a, b)

    def test_number_of_pairs(self):
        series = TickSeries((0,1), 10)
        self.assertEqual(10, len(list(series.pairs)))

