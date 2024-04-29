import pygame, sys, math

class HealthBar():
    def __init__(self, baseImage, position = [0, 0]):
        self.baseImage = pygame.image.load("Bro/Images/HealthBar.png")
        self.image = self.baseImage
        self.rect = self.image.get_rect(topleft = position)

    def update(self, image):
        self.image = image
        self.rect = self.image.get_rect(topleft = self.rect.topleft)
