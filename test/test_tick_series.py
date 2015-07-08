# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:26:14 2015

@author: jack
"""
import unittest

from tick_series import TickSeries

class TestTickSeries(unittest.TestCase):
    def test_number_of_points(self):
        series = TickSeries((0,1), 10)
        self.assertEqual(11, len(set(series.ticks)))

