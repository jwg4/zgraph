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
            stl.Facet(self.normal(self.a, self.b, self.c),
                      (self.a, self.b, self.c)),        
            stl.Facet(self.normal(self.a, self.c, self.d),
                      (self.a, self.c, self.d))        
        ]

    @staticmethod
    def normal(v1, v2, v3):
        return stl.Vector3d(0, 0, 0)
        