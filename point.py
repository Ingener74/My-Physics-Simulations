#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Point:
    """ Класс точки """
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
        
    def __eq__(self, right):
        return self._x == right._x and self._y == right._y
    
    def __ne__(self, right):
        return self._x != right._x or self._y != right._y
        
    def __add__(self, right):
        if not isinstance(right, (Point,int,float)): 
            raise TypeError("invalid type")
        if isinstance(right, (int, float)): 
            return Point(self._x + right, self._y + right)
        else: 
            return Point(self._x + right._x, self._y + right._y)

    def __sub__(self, right):
        if not isinstance(right, (Point,int,float)):
            raise TypeError("invalid type")
        if isinstance(right, (int, float)):
            return Point(self._x - right, self._y - right)
        else:
            return Point(self._x - right.x, self._y - right.y)

    def __mul__(self, right):
        if not isinstance(right, (Point,int, float)):
            raise TypeError("invalid type")
        if isinstance(right, (int, float)):
            return Point(self._x * right, self._y * right)
        else:
            return Point(self._x * right.x, self._y * right.y)

    def __div__(self, right):
        if not isinstance(right, (Point,int, float)):
            raise TypeError("invalid type")
        if isinstance(right, (int, float)):
            if right == 0: raise ArithmeticError("right is zero")
            return Point(self._x / right, self._y / right)
        else:
            if right.x == 0 or right.y == 0: raise ArithmeticError("right is zero")
            return Point(self._x / right.x, self._y / right.y)
        
    def normalize(self, right):
        L = self.lenght(right)
        return Point((right._x - self._x) / L, (right._y - self._y) / L)

    def len(self):
        return math.sqrt(self._y ** 2 + self._x ** 2)
    
    def lenght(self, right):
        return math.sqrt((self._y - right._y) ** 2 + (self._x - right._x) ** 2)
    
    def toTuple(self):
        return (int(self._x), int(self._y))
    
    def __repr__(self):
        return "Point[%s x %s]" % (self._x, self._y)
    
    def __str__(self):
        return "Point[%s x %s]" % (self._x, self._y)