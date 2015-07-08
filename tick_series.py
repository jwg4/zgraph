# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:21:31 2015

@author: jack
"""

class TickSeries(object):
    def __init__(self, range_, n):
        self.range = range_
        self.n = n
        
    @property
    def ticks(self):
        step_size = (self.range[1] - self.range[0]) + 0.0 / self.n
        start = self.range[0]
        return [ (start + n * step_size) for n in range(0, self.n + 1) ]

    @property
    def pairs(self):
        t = self.ticks
        for n in range(0, self.n):
            yield (t[n], t[n+1]) 
    