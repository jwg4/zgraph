# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:57:55 2015

@author: jack
"""

import unittest

import stl

from side_face import XFace, YFace
from tick_series import TickSeries

class MockZGraph(object):
    def __init__(self, f, range_, series):
        self.vector_f = f
        self.x_range = range_
        self.x_series = series
        self.y_range = range_
        self.y_series = series

class TestSideFace(unittest.TestCase):
    def test_basic_steplike_face(self):
        def f(x,y):
            return stl.Vector3d(x, y, 2 if abs(x) > 1 else 1)
        range_ = (-3, 3)
        x_series = TickSeries(range_, 3)
        graph = MockZGraph(f, range_, x_series)
        
        front_face = XFace(range_[0], stl.Vector3d(0, -1, 0), True, graph)
        
        self.assertEqual(len(front_face.face), 6)
        
    def test_basic_steplike_yface(self):
        def f(x,y):
            return stl.Vector3d(x, y, 2 if abs(y) > 1 else 1)
        range_ = (-3, 3)
        y_series = TickSeries(range_, 3)
        graph = MockZGraph(f, range_, y_series)
        
        left_face = YFace(range_[0], stl.Vector3d(-1, 0, 0), False, graph)
        
        self.assertEqual(len(left_face.face), 6)