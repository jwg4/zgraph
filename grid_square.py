# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 08:55:40 2015

@author: jack
"""

import stl

class GridSquare(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    @property
    def facets(self):
        return [
            stl.Facet(stl.Vector3d(0, 0, 0), (self.a, self.b, self.c)),        
            stl.Facet(stl.Vector3d(0, 0, 0), (self.a, self.c, self.d))        
        ]
