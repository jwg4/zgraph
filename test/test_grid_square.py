# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 08:57:05 2015

@author: jack
"""
from math import sqrt

import unittest

from stl import Vector3d, Facet

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
        b = Vector3d(1, 0, 1)
        c = Vector3d(1, 1, 1)
        d = Vector3d(0, 1, 1)
        gs = GridSquare(a, b, c, d)
        self.assertEqual(len(gs.facets), 2)
        vertical = Vector3d(0, 0, 1)
        self.assertEqual(gs.facets[0], Facet(vertical, (a, b, c)))
        
    def test_normal(self):
        a = Vector3d(1, 0, 0)
        b = Vector3d(0, 1, 0)
        c = Vector3d(0, 0, 1)
        expected = Vector3d(1/sqrt(3), 1/sqrt(3), 1/sqrt(3))
        self.assertEqual(GridSquare.normal(a, b, c), expected)
        
    def test_normal2(self):
        a = Vector3d(0, 0, 1)
        b = Vector3d(1, 0, 1)
        c = Vector3d(1, 1, 1)
        expected = Vector3d(0, 0, 1)
        self.assertEqual(GridSquare.normal(a, b, c), expected)
        
    def test_normal_jk(self):
        a = Vector3d(0, 0, 0)
        b = Vector3d(0, 1, 0)
        c = Vector3d(0, 0, 1)
        expected = Vector3d(1, 0, 0)
        self.assertEqual(GridSquare.normal(a, b, c), expected)
        
    def test_normal_ij(self):
        a = Vector3d(0, 0, 0)
        b = Vector3d(1, 0, 0)
        c = Vector3d(0, 1, 0)
        expected = Vector3d(0, 0, 1)
        self.assertEqual(GridSquare.normal(a, b, c), expected)
        
