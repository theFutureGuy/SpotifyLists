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
            
