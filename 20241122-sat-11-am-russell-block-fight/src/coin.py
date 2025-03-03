import pygame
from pygame.sprite import Sprite
import random as r
from config import *
class Coin(Sprite):
    def __init__(self, screen, x,y):
        super().__init__()
        self.x = r.randint(0,1000)
        self.y = r.randint(0,750)
        self.screen = screen

        self.images = []
        for i in range(1, 2):
            image = pygame.image.load(f"assets/coin_{i}.png")
            self.images.append(image)

        self.speed = 5
        self.image_index = 0
        self.rect = pygame.Rect(self.x, self.y, self.images[0].get_width(), self.images[0].get_height())
        self.timer = ANIMATIONDELAY

    def update(self):

        image = self.images[self.image_index]
        self.timer = - 1
        if self.timer == 0:
            self.image_index += 1
            if self.image_index == 4:
                self.image_index = 0
            self.timer = ANIMATIONDELAY
        self.x -= self.speed
        if TESTING:
            pygame.draw.rect(self.screen, (255, 0, 255), self.rect)
        self.rect.x = self.x

        self.screen.blit(image, (self.x, self.y))
