# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:19:57 2015

@author: jack
"""

import stl

class SideFace(object):
    @staticmethod
    def triangulate(normal, vertices):
        if len(vertices) < 3:
            return []
        facet1 = stl.Facet(normal, vertices[:3])
        remaining_facets = vertices[:1] + vertices[2:]
        return [facet1] + SideFace.triangulate(normal, remaining_facets)
    
    
    def make_face(self,
                    first_corner, second_corner,
                    vectors):
        if self.backwards:
            return self.triangulate(self.normal,
                                    [first_corner] +
                                    [second_corner] + 
                                    list(reversed(vectors))
                                    )
        else:
            return self.triangulate(self.normal,
                                    [first_corner] +
                                    vectors +
                                    [second_corner]
                                    )        
            
class YFace(SideFace):
    def __init__(self, x, normal, backwards, graph):
        self.x = x
        self.normal = normal
        self.backwards = backwards
        self.y_start = graph.y_range[0]
        self.y_end = graph.y_range[1]
        self.y_ticks = graph.y_series.ticks
        self.f = graph.vector_f
    
    @property
    def face(self):
        value_vectors = [ 
                            self.f(self.x, y)
                            for y in self.y_ticks
                        ]
        base_vectors =  [
                            stl.Vector3d(self.x, y, 0)
                            for y in self.y_ticks
                        ]
        facets = []
        for i in range(0, len(base_vectors) - 1):
            if self.backwards:
                points = [base_vectors[i],
                          value_vectors[i],
                          value_vectors[i+1],
                          base_vectors[i+1]]
            else:
                points = [base_vectors[i],
                          base_vectors[i+1],
                          value_vectors[i+1],
                          value_vectors[i]]                
            facets = facets + self.triangulate(self.normal, points)
        return facets

class XFace(SideFace):
    def __init__(self, y, normal, backwards, graph):
        self.y = y
        self.normal = normal
        self.backwards = backwards
        self.x_start = graph.x_range[0]
        self.x_end = graph.x_range[1]
        self.x_ticks = graph.x_series.ticks
        self.f = graph.vector_f
    
    @property
    def face(self):
        value_vectors = [ 
                            self.f(x, self.y)
                            for x in self.x_ticks
                        ]
        base_vectors =  [
                            stl.Vector3d(x, self.y, 0)
                            for x in self.x_ticks
                        ]
        facets = []
        for i in range(0, len(base_vectors) - 1):
            if self.backwards:
                points = [base_vectors[i],
                          value_vectors[i],
                          value_vectors[i+1],
                          base_vectors[i+1]]
            else:
                points = [base_vectors[i],
                          base_vectors[i+1],
                          value_vectors[i+1],
                          value_vectors[i]]                
            facets = facets + self.triangulate(self.normal, points)
        return facets
