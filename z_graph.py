# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 14:03:34 2015

@author: jack
"""

import stl

class ZGraph(object):
    def __init__(self, xrange, yrange, f, n):
        self.xrange = xrange
        self.yrange = yrange
        self.f = f
        self.n = n
        
    def solid_output(self):
        return stl.Solid(name="ZGraph")
    
    @staticmethod
    def triangulate(normal, vertices):
        if len(vertices) < 3:
            return []
        facet1 = stl.Facet(normal, vertices[:3])
        remaining_facets = vertices[:1] + vertices[2:]
        return [facet1] + ZGraph.triangulate(normal, remaining_facets)
        
        
        
        