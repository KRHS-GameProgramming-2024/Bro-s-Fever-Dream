import pygame, sys, random, math

class Hud():
    def __init__(self, baseText, startPos=[0, 0]):
        self.font = pygame.font.Font(None, 50)
        self.baseText = baseText
        self.image = self.font.render("I protect my eyes", 1, (10, 10, 10))
        self.rect = self.image.get_rect(topleft=startPos)
        # ~ background.blit(text, textpos)

    def update(self, Health):
        text = self.baseText + str(Health) 
        self.image = self.font.render(text, 1, (10, 10, 10))
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
