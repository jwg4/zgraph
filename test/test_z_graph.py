# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 14:08:38 2015

@author: jack
"""

import unittest

import stl

from z_graph import ZGraph

class TestZGraph(unittest.TestCase):
    def test_solid_output(self):
        def const_2(x, y):
            return 2
        graph = ZGraph((0,1), (0,1), const_2, 1)
        top_left_front     = stl.Vector3d(0, 0, 2)
        top_right_front    = stl.Vector3d(1, 0, 2)
        top_left_back      = stl.Vector3d(0, 1, 2)
        top_right_back     = stl.Vector3d(1, 1, 2)
        bottom_left_front  = stl.Vector3d(0, 0, 0)
        bottom_right_front = stl.Vector3d(1, 0, 0)
        bottom_left_back   = stl.Vector3d(0, 1, 0)
        bottom_right_back  = stl.Vector3d(1, 1, 0)
        facets = [
             # Top
            stl.Facet(stl.Vector3d(0, 0, 1),
                      (top_left_front, top_right_front, top_right_back)),    
            stl.Facet(stl.Vector3d(0, 0, 1),
                      (top_right_back, top_left_back, top_left_front)),    
            # Bottom
            stl.Facet(stl.Vector3d(0, 0, -1),
                      (bottom_left_front, bottom_right_back, bottom_right_front)),    
            stl.Facet(stl.Vector3d(0, 0, -1),
                      (bottom_right_back, bottom_left_back, bottom_left_front)),    
        ]
        expected = stl.Solid("ZGraph", facets)
    
    def test_triangulate_square(self):
        top_left_front     = stl.Vector3d(0, 0, 2)
        top_right_front    = stl.Vector3d(1, 0, 2)
        top_left_back      = stl.Vector3d(0, 1, 2)
        top_right_back     = stl.Vector3d(1, 1, 2)
        corners = [top_left_front,
                   top_left_back,
                   top_right_back,
                   top_right_front]  
        normal = stl.Vector3d(0, 0, 1)
        result = ZGraph.triangulate(normal, corners)
        self.assertEqual(len(result), 2)
        
    def test_triangulate_triangle(self):
        normal = stl.Vector3d(1, 1, 1)
        a = stl.Vector3d(1, 0, 0)
        b = stl.Vector3d(0, 1, 0)
        c = stl.Vector3d(0, 0, 1)
        expected = stl.Facet(normal, (a, b, c))
        result = ZGraph.triangulate(normal, (a, b, c))
        self.assertEqual(result[0], expected)
    