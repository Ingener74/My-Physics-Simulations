#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, pygame
from point import Point
from node import Node

class Ball():
    def __init__(self, center, radius, nodesColor, linesColor, nodeCount = 36):
        self._center      = center
        self._nodes       = []
        self._nodesColor  = nodesColor
        self._linesColor  = linesColor
        
        self._pressure    = 80000.0
        
        for i in xrange(0, nodeCount):
            angle = 2.0*math.pi * i / nodeCount
            N = Node(Point(self._center._x + radius * math.cos(angle), self._center._y + radius * math.sin(angle)), 10, 1)
            N.addExternalForce(self.pump)
            self._nodes.append(N)
            
        for node, idx in zip(self._nodes, range(0, len(self._nodes))):
            node.addNode(self._nodes[(idx - 1) % len(self._nodes)])
            node.addNode(self._nodes[(idx + 1) % len(self._nodes)])
            
    def draw(self, surface):
        for node in self._nodes:
            for intNode in node._nodes:
                pygame.draw.line(surface, self._linesColor, node._pos.toTuple(), intNode._pos.toTuple())
            pygame.draw.circle(surface, self._nodesColor, node._pos.toTuple(), 2)
            
    def update(self, dt):
        self._center = Point()
        for node in self._nodes:
            node.update(dt)
            self._center += node._pos
        self._center._x /= len(self._nodes)
        self._center._y /= len(self._nodes)
        
    def area(self):
        sum = 0.0
        for node, idx in zip(self._nodes, range(0, len(self._nodes))):
            next_idx = (idx + 1) % len(self._nodes)
            sum += (node._pos._x + self._nodes[next_idx]._pos._x)*(node._pos._y - self._nodes[next_idx]._pos._y)
        return 0.5 * abs(sum)

    def pump(self, node):
        dP = self._pressure / self.area()
        direction = self._center.normalize(node._pos)
        return direction * dP
    
def gravity(node):
    return Point(0, 9.8)

def floor(node):
    return Point(0.0, 0.0 if node._pos._y < 500.0 else -10 * node._pos._y)

def main():
    WIDTH                = 800
    HEIGHT               = 600
    BG_COLOR             = (150, 200, 255)

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncing Ball")
    
    surface = pygame.Surface((WIDTH, HEIGHT))
    
    B = Ball(Point(200, 200), 100, (255, 0, 0), (0, 255, 0))
    for node in B._nodes:
        node.addExternalForce(gravity)
        node.addExternalForce(floor)
    
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                raise SystemExit
            
        surface.fill(BG_COLOR)
        B.update(1.0 / 30.0)
        B.draw(surface)
            
        window.blit(surface, (0, 0))
        pygame.display.update()

if __name__ == '__main__':
    main()