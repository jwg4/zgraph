# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 14:03:34 2015

@author: jack
"""

import stl

from grid_square import GridSquare
from tick_series import TickSeries

class ZGraph(object):
    rightw = stl.Vector3d(1, 0, 0)
    leftw = stl.Vector3d(-1, 0, 0)
    backwards = stl.Vector3d(0, 1, 0)
    forwards = stl.Vector3d(0, -1, 0)
    up = stl.Vector3d(0, 0, 1)
    down = stl.Vector3d(0, 0, -1)

    def __init__(self, x_range, y_range, f, n):
        self.x_range = x_range
        self.y_range = y_range
        self.f = f
        self.__x_series = TickSeries(x_range, n)
        self.__y_series = TickSeries(y_range, n)
        
    def __grid_squares(self):
        for y1, y2 in self.__y_series.pairs:
            for x1, x2 in self.__x_series.pairs:
                yield GridSquare(*
                    [
                        self.__vector_f(*pair)
                            for pair in
                            [
                                (x1, y1),    
                                (x2, y1),    
                                (x2, y2),    
                                (x1, y2) 
                            ]
                    ]                                    
                )
        
    @property
    def __top(self):
        return [ f
                    for sq in self.__grid_squares()
                        for f in sq.facets 
               ]
            
    @property
    def __bottom(self):
        return self.triangulate(
            self.down,
            (
                stl.Vector3d(self.x_range[0], self.y_range[0], 0),
                stl.Vector3d(self.x_range[0], self.y_range[1], 0),
                stl.Vector3d(self.x_range[1], self.y_range[1], 0),
                stl.Vector3d(self.x_range[1], self.y_range[0], 0)
            )
        )
            
    def __vector_f(self, x, y):
        return stl.Vector3d(x, y, self.f(x, y))            
            
    def __make_face(self,
                    normal,
                    first_corner, second_corner,
                    vectors,
                    backwards=False):
        if backwards:
            return self.triangulate(normal,
                                    [first_corner] +
                                    [second_corner] + 
                                    list(reversed(vectors))
                                   )
        else:
            return self.triangulate(normal,
                                    [first_corner] +
                                    vectors +
                                    [second_corner])        
            
    def __x_face(self, y, normal, backwards):
        first_corner = stl.Vector3d(self.x_range[0], y, 0)
        second_corner = stl.Vector3d(self.x_range[1], y, 0)
        value_vectors = [ 
                            self.__vector_f(x, y)
                            for x in self.__x_series.ticks
                        ]
        return self.__make_face(normal,
                                first_corner, 
                                second_corner, 
                                value_vectors,
                                backwards)        

    @property
    def __front(self):
        return self.__x_face(self.y_range[0], self.forwards, True)

    @property
    def __back(self):
        return self.__x_face(self.y_range[1], self.backwards, False)

    def __y_face(self, x, normal, backwards):
        first_corner = stl.Vector3d(x, self.y_range[0], 0)
        second_corner = stl.Vector3d(x, self.y_range[1], 0)
        value_vectors = [ 
                            self.__vector_f(x, y)
                            for y in self.__y_series.ticks
                        ]
        return self.__make_face(normal,
                                first_corner, 
                                second_corner, 
                                value_vectors,
                                backwards)        
    @property
    def __right(self):
        return self.__y_face(self.x_range[1], self.rightw, True)
        
    @property
    def __left(self):
        return self.__y_face(self.x_range[0], self.leftw, False)
        
    def solid_output(self):
        return stl.Solid(name="ZGraph",
                         facets = self.__top + 
                                  self.__bottom + 
                                  self.__front + 
                                  self.__right +
                                  self.__back +
                                  self.__left)
    
    @staticmethod
    def triangulate(normal, vertices):
        if len(vertices) < 3:
            return []
        facet1 = stl.Facet(normal, vertices[:3])
        remaining_facets = vertices[:1] + vertices[2:]
        return [facet1] + ZGraph.triangulate(normal, remaining_facets)
