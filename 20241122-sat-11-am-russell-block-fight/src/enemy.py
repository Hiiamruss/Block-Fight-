import pygame
import random as r
from config import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, x_coordinate, y_coordinate, direction):
        super().__init__()
        self.screen = screen
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.direction = direction

        self.enemy_number = r.randint(1, 4)
        self.images = []

        for i in range(1, 5):
            self.image = pygame.image.load(f"assets/enemy_{i}.png")
            self.image = pygame.transform.scale(self.image, (50 * 1.25, 50))
            self.images.append(self.image)
        self.speed = r.randint(2, 8)
        self.image_index = 0
        self.rect = pygame.Rect(self.x_coordinate, self.y_coordinate, 72, 50)
        self.enemy_animation_timer = ANIMATIONDELAY

    def update(self):
        self.rect.x = self.x_coordinate
        self.rect.y = self.y_coordinate
        if TESTING:
            pygame.draw.rect(self.screen, (0, 255, 0), self.rect)

        image = self.images[self.image_index]

        if self.direction == LEFT:
            self.x_coordinate -= self.speed
        elif self.direction == RIGHT:
            self.x_coordinate += self.speed
        elif self.direction == UP:
            self.y_coordinate -= self.speed
        elif self.direction == DOWN:
            self.y_coordinate += self.speed

        self.enemy_animation_timer -= 1

        if self.enemy_animation_timer == 0:
            self.image_index += 1
            self.enemy_animation_timer = ANIMATIONDELAY


            if self.image_index == len(self.images):
                self.image_index = 0


        self.screen.blit(image, (self.x_coordinate, self.y_coordinate,))