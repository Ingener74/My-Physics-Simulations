#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, pygame
from point import Point
from node import Node

nodesGrid = [
        '211111111111111111111111111111111111112',
        '000000010000000000000000001000000000000',
        '211111111111111111111111111111111111112',
        '100000000000000000000000000000000000001',
        '100000000000000000000000000000000000201',
        '100000000000000000000000000000000000101',
        '100000000000000000000000000000000000101',
        '100000000000000000000000000000000000101',
        '100000000000000000000000000000000000101',
        '100000000000000000000000000000000000101',
        '100000000000000000000000000000000000111',
        '100000000000000000000000000000000000001',
        '100000000000000000000000000000000000001',
        '100000000000000000000000000000000000001',
        '100000000000000000000000000000000000001',
        '100000000000000000000000000000000000001',
        ]

def gravity(node):
    return Point(0, 9.8)

def main():
    WIDTH                = 800
    HEIGHT               = 600
    NODE_COLOR           = (0, 0, 0)
    FIX_NODE_COLOR       = (255, 0, 0)
    LINE_COLOR           = (255, 255, 0)
    BG_COLOR             = (150, 200, 255)
                         
    NODE_X0              = 10
    NODE_Y0              = 10
                         
    NODE_X_STEP          = 20
    NODE_Y_STEP          = 20
                         
    NODE_MASS            = 10.0
    
    NODE_CONNECT_RADIUS  = 21
    
    NODE_C               = 2
    
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Node grid test")
    
    surface = pygame.Surface((WIDTH, HEIGHT))
    surface.fill(pygame.Color(150, 200, 255))
    
    x = NODE_X0
    y = NODE_Y0
    nodes = []
    connectRadius = NODE_CONNECT_RADIUS

    for nodeLevel in nodesGrid:
        x = NODE_X0
        for node in nodeLevel:
            if node != '0':
                N = Node(Point(x, y), NODE_MASS, NODE_C, node == '2')
                N.addExternalForce(gravity)
                nodes.append(N)
            x += NODE_X_STEP
        y += NODE_Y_STEP
        
    for node in nodes:
        for nodeInt in nodes:
            if node.length(nodeInt) < connectRadius and node != nodeInt:
                node.addNode(nodeInt)
                
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                raise SystemExit
            
        for node in nodes:
            node.update(1.0 / 30.0)
        
        surface.fill(BG_COLOR)
        for node in nodes:
            for intNode in node._nodes:
                pygame.draw.line(surface, LINE_COLOR, node._pos.toTuple(), intNode._pos.toTuple())
            pygame.draw.circle(surface, FIX_NODE_COLOR if node._fixed else NODE_COLOR , node._pos.toTuple(), 2)
            
        window.blit(surface, (0, 0))
        pygame.display.update()

if __name__ == '__main__':
    main()
