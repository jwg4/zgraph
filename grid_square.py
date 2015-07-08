# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 08:55:40 2015

@author: jack
"""
from math import sqrt

import stl

class ZeroVectorError(ValueError):
    pass

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
    def __normalize(v):
        size = sqrt(v[0]**2 + v[1]**2 + v[2]**2)
        if size == 0:
            raise ZeroVectorError("Tried to normalize a vector with size zero: %s"
                             % str(v))
        return stl.Vector3d(v[0]/size, v[1]/size, v[2]/size)

    @staticmethod
    def normal(v1, v2, v3):
        u1 = (v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2])
        u2 = (v3[0] - v1[0], v3[1] - v1[1], v3[2] - v1[2])
        x = u1[1] * u2[2] - u1[2] * u2[1]        
        y = u1[2] * u2[0] - u1[0] * u2[2]        
        z = u1[0] * u2[1] - u1[1] * u2[0]       
        try:
            u = GridSquare.__normalize(stl.Vector3d(x, y, z))
        except ZeroVectorError:
            raise ValueError(("Couldn't calculate the normal to the vectors" 
                              + "%s and %s - are they colinear? "
                              + "The triangle points are %s, %s and %s.")
                             % (u1, u2, v1, v2, v3))
        return u