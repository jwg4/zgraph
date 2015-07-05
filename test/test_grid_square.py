# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 08:57:05 2015

@author: jack
"""

import unittest

from stl import Vector3d

from grid_square import GridSquare

class TestGridSquare(unittest.TestCase):
    def test_construct(self):
        a = Vector3d(0, 0, 1)
        b = Vector3d(0, 1, 1)
        c = Vector3d(1, 1, 1)
        d = Vector3d(1, 0, 1)
        gs = GridSquare(a, b, c, d)
        self.assertIsNotNone(gs)
        
    def test_facets(self):
        a = Vector3d(0, 0, 1)
        b = Vector3d(0, 1, 1)
        c = Vector3d(1, 1, 1)
        d = Vector3d(1, 0, 1)
        gs = GridSquare(a, b, c, d)
        self.assertEqual(len(gs.facets), 2)