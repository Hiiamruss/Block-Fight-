import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x_coordinate, y_coordinate, size, main):
        super().__init__()
        self.screen = screen
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.size = size
        self.right_image_list = []
        self.left_image_list = []
        for i in range(1, 5):
            image = pygame.image.load(f"assets/player_{i}.png")
            image = pygame.transform.scale(image, (1.25 * self.size, size))
            self.right_image_list.append(image)

            image = pygame.transform.flip(image, True, False)
            self.left_image_list.append(image)


        self.speed = 5

        self.direction = RIGHT
        self.image_index = 0
        self.player_animation_timer = ANIMATIONDELAY

        self.rect = pygame.Rect(self.x_coordinate, self.y_coordinate, 1.25 * self.size, size)

        self.main = main

    def update(self):
        if self.main.score >= 20:
            self.speed = 7
        self.rect.x = self.x_coordinate
        self.rect.y = self.y_coordinate
        if TESTING:
            pygame.draw.rect(self.screen, (0, 255, 0), self.rect)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            self.direction = UP
            self.y_coordinate -= self.speed
        elif keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            self.direction = DOWN
            self.y_coordinate += self.speed

        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.direction = LEFT
            self.x_coordinate -= self.speed
        elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.direction = RIGHT
            self.x_coordinate += self.speed

        if self.direction == LEFT:
            image = self.left_image_list[self.image_index]
        else:
            image = self.right_image_list[self.image_index]

        self.player_animation_timer -= 1

        if self.player_animation_timer == 0:
            self.image_index += 1
            self.player_animation_timer = ANIMATIONDELAY

            if self.image_index == len(self.left_image_list):
                self.image_index = 0

        self.screen.blit(image, (self.x_coordinate, self.y_coordinate))