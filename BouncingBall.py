#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math, pygame
from point import Point

def main():
    WIDTH                = 800
    HEIGHT               = 600
    BG_COLOR             = (150, 200, 255)

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncing Ball")
    
    surface = pygame.Surface((WIDTH, HEIGHT))
    
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                raise SystemExit
            
        surface.fill(BG_COLOR)
            
        window.blit(surface, (0, 0))
        pygame.display.update()

if __name__ == '__main__':
    main()