import pygame
import math
import numpy as np
import random



class pongGame:    
    def __init__(self, h, w, draw=True):
        """ Initializing parameters """
        # window height
        self.h = h
        # window width
        self.w = w
        # If you intend to use for visualization, set draw to True
        if (draw):
            pygame.init()
            self.window = pygame.display.set_mode((self.h, self.w))
        else:
            self.window = None
            
def draw(self):
        self.window.fill(0)

        pygame.draw.rect(self.window, (255, 255, 255),
                         (5, self.y1, 10, self.paddle_length))
        pygame.draw.rect(self.window, (255, 255, 255),
                         (self.w-15, self.y2, 10, self.paddle_length))
        pygame.draw.circle(self.window, (255, 255, 255),
                           (self.xball, self.yball), 5)
        pygame.display.flip()