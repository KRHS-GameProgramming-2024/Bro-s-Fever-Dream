import pygame, sys, math

class ImageHud():
    def __init__(self, baseImage, position = [0, 0]):
        self.baseImage = pygame.image.load("BaseImage.png")
        self.image = self.baseImage
        self.rect = self.image.get_rect(topleft = position)

    def update(self, image):
        self.image = image
        self.rect = self.image.get_rect(topleft = self.rect.topleft)
