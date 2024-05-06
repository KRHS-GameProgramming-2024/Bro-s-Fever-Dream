import pygame, math, sys, random

class Background():
    def __init__(self, image):
        self.image = pygame.image.load("Backgrounds/"+image)
        self.rect = self.image.get_rect()
