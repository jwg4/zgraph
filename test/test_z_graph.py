# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 14:08:38 2015

@author: jack
"""

import unittest

from math import sqrt

import stl

from z_graph import ZGraph

class TestZGraph(unittest.TestCase):
    def test_solid_output_for_const_graph(self):
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
        top = ZGraph.triangulate(
            stl.Vector3d(0, 0, 1),
            (
                top_left_front,
                top_right_front,
                top_right_back,
                top_left_back
            )
        )
        bottom = ZGraph.triangulate(
            stl.Vector3d(0, 0, -1),
            (
                bottom_left_front,
                bottom_left_back,
                bottom_right_back,
                bottom_right_front
            )
        )
        front = ZGraph.triangulate(
            stl.Vector3d(0, -1, 0),
            (
                bottom_left_front,
                bottom_right_front,
                top_right_front,
                top_left_front
            )        
        )
        right = ZGraph.triangulate(
            stl.Vector3d(1, 0, 0),
            (
                bottom_right_front,
                bottom_right_back,
                top_right_back,
                top_right_front
            )
        )
        back = ZGraph.triangulate(
            stl.Vector3d(0, 1, 0),
            (
                bottom_left_back,
                top_left_back,
                top_right_back,
                bottom_right_back
            )        
        )
        left = ZGraph.triangulate(
            stl.Vector3d(-1, 0, 0),
            (
                bottom_left_front,
                top_left_front,
                top_left_back,
                bottom_left_back
            )
        )
        facets = top + bottom + front + right + back + left
        expected = stl.Solid("ZGraph", facets)
        
        self.assertEqual(graph.solid_output(), expected)
    
    def test_solid_output_for_simple_graph(self):
        def simple(x, y):
            if x > 0.5 and y > 0.5:            
                return 2
            else:
                return 1
        graph = ZGraph((0,1), (0,1), simple, 1)

        top_left_front     = stl.Vector3d(0, 0, 1)
        top_right_front    = stl.Vector3d(1, 0, 1)
        top_left_back      = stl.Vector3d(0, 1, 1)
        top_right_back     = stl.Vector3d(1, 1, 2)
        bottom_left_front  = stl.Vector3d(0, 0, 0)
        bottom_right_front = stl.Vector3d(1, 0, 0)
        bottom_left_back   = stl.Vector3d(0, 1, 0)
        bottom_right_back  = stl.Vector3d(1, 1, 0)
        top = [ 
                stl.Facet(
                    stl.Vector3d(0, -1/sqrt(2), 1/sqrt(2)),
                    [
                        top_left_front, 
                        top_right_front,
                        top_right_back
                    ]                
                ),
                stl.Facet(
                    stl.Vector3d(-1/sqrt(2), 0, 1/sqrt(2)),
                    [
                        top_left_front, 
                        top_right_back,
                        top_left_back
                    ]                
                ),
              ]        
        bottom = ZGraph.triangulate(
            stl.Vector3d(0, 0, -1),
            (
                bottom_left_front,
                bottom_left_back,
                bottom_right_back,
                bottom_right_front
            )
        )
        front = ZGraph.triangulate(
            stl.Vector3d(0, -1, 0),
            (
                bottom_left_front,
                bottom_right_front,
                top_right_front,
                top_left_front
            )        
        )
        right = ZGraph.triangulate(
            stl.Vector3d(1, 0, 0),
            (
                bottom_right_front,
                bottom_right_back,
                top_right_back,
                top_right_front
            )
        )
        back = ZGraph.triangulate(
            stl.Vector3d(0, 1, 0),
            (
                bottom_left_back,
                top_left_back,
                top_right_back,
                bottom_right_back
            )        
        )
        left = ZGraph.triangulate(
            stl.Vector3d(-1, 0, 0),
            (
                bottom_left_front,
                top_left_front,
                top_left_back,
                bottom_left_back
            )
        )
        facets = top + bottom + front + right + back + left
        expected = stl.Solid("ZGraph", facets)
        
        self.assertEqual(graph.solid_output(), expected)
    
    def test_nb_vertices_for_const_graph(self):
        def const_2(x, y):
            return 2
        graph = ZGraph((0,1), (0,1), const_2, 10)
        self.assertEqual(246, len(graph.solid_output().facets))

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
    