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
        
        for i in xrange(0, nodeCount):
            angle = 2.0*math.pi * i / nodeCount
            N = Node(Point(self._center._x + radius * math.cos(angle), self._center._y + radius * math.sin(angle)), 10, 1)
            self._nodes.append(N)
            
        for node, idx in zip(self._nodes, range(0, len(self._nodes))):
            node.addNode(self._nodes[(idx - 1) % len(self._nodes)])
            node.addNode(self._nodes[(idx + 1) % len(self._nodes)])
            
    def draw(self, surface):
        for node in self._nodes:
            for intNode in node._nodes:
                pygame.draw.line(surface, self._linesColor, node._pos.toTuple(), intNode._pos.toTuple())
            pygame.draw.circle(surface, self._nodesColor, node._pos.toTuple(), 2)
            
    def pump(self):
        return Point()
    
def gravity(node):
    return Point(0, 9.8)

def main():
    WIDTH                = 800
    HEIGHT               = 600
    BG_COLOR             = (150, 200, 255)

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncing Ball")
    
    surface = pygame.Surface((WIDTH, HEIGHT))
    
    B = Ball(Point(200, 200), 100, (255, 0, 0), (0, 255, 0))
    
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                raise SystemExit
            
        surface.fill(BG_COLOR)
        
        B.draw(surface)
            
        window.blit(surface, (0, 0))
        pygame.display.update()

if __name__ == '__main__':
    main()