import pygame
import random as r
from config import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x_coordinate, y_coordinate, direction):
        super().__init__()
        self.screen = screen
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.direction = direction



        if direction == UP:
            self.image = pygame.image.load(f"assets/bullet_up.png")
        if direction == DOWN:
            self.image = pygame.image.load(f"assets/bullet_down.png")
        if direction == LEFT:
            self.image = pygame.image.load(f"assets/bullet_left.png")
        if direction == RIGHT:
            self.image = pygame.image.load(f"assets/bullet_right.png")
        self.speed = 10

        self.rect = pygame.Rect(self.x_coordinate, self.y_coordinate, self.image.get_width(), self.image.get_height())
    def update(self):
        self.rect.x = self.x_coordinate
        if TESTING:
            pygame.draw.rect(self.screen, (0, 255, 0), self.rect)

        self.screen.blit(self.image, (self.x_coordinate, self.y_coordinate, ))

        if self.direction == LEFT:
            self.x_coordinate -= self.speed
        elif self.direction == RIGHT:
            self.x_coordinate += self.speed
        elif self.direction == DOWN:
            self.y_coordinate += self.speed
        elif self.direction == UP:
            self.y_coordinate -= self.speed