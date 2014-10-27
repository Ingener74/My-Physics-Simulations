#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from point import Point

class Node:
    """ Node class """
    def __init__(self, pos, mass, C, fixed=False):
        self._pos        = pos
        self._vel        = Point()
        self._nodes      = []
        self._lenths     = []
        self._fixed      = fixed
        self._mass       = mass
        self._C          = C
        self._extForces  = []
        
    def __eq__(self, r):
        return self._pos == r._pos
    
    def __ne__(self, r):
        return self._pos != r._pos

    def update(self, dt):
        if self._fixed:
            return 0.0
        else:
            ef = Point()
            for node, L in zip(self._nodes, self._lenths):
                ef += self.getElasticForce(node, L)
            ff = self.getFrictionalForce()

            efs = Point()
            for f in self._extForces:
                efs += f(self)
            
            self._vel += (ef + ff + efs / self._mass) * dt
            self._pos += self._vel * dt
            
            return self._pos.len()
    
    def addNode(self, node):
        self._nodes.append(node)
        self._lenths.append(self.length(node))

    def __repr__(self):
        return "Node[%s: %s, %s]" % (self._pos, len(self._nodes), self._fixed)
    def __str__(self):
        return "Node[%s: %s, %s]" % (self._pos, len(self._nodes), self._fixed)
    
    def length(self, node):
        return math.sqrt( (node._pos._y - self._pos._y) ** 2 + (node._pos._x - self._pos._x)** 2 )
    
    def getElasticForce(self, node, node_distance):
        L = self._pos.lenght(node._pos)
        Lf = 0  if L < node_distance else L - node_distance
        
        direction = self._pos.normalize(node._pos)
        
        return Point(direction._x * self._C * Lf, direction._y * self._C * Lf)
    
    def getFrictionalForce(self):
        return Point(-0.1 * self._vel._x , -0.1 * self._vel._y)

    def addExternalForce(self, force):
        self._extForces.append(force)